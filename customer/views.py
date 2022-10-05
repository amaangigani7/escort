from django.shortcuts import render, redirect
from rest_framework import status, authentication, permissions, generics
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
# from django.contrib.auth import login
from rest_framework import permissions
# from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import *
from .serializers import *
from .utils import *
from django.conf import settings
from django.db.models import Q

# # Create your views here.


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, customer):
        token = super().get_token(customer)

        # Add custom claims
        token['user_name'] = customer.user_name
        token['email'] = customer.email
        token['password'] = customer.password
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        if '.' in request.data['user_name']:
            return Response({"message": 'Username cannot have a "."'}, status.HTTP_200_OK)
        c = Customer.objects.filter(email=request.data['email'])
        if len(c) > 0:
            if c[0].is_active:
                return Response({"message": 'Email already registered! Try logging in!'}, status.HTTP_200_OK)
            else:
                while True:
                    auth_token = str(uuid.uuid4())
                    if not Customer.objects.filter(verification_token=auth_token).first():
                        break
                customer = Customer.objects.get(email=request.data['email'])
                customer.verification_token = auth_token
                customer.save()
                SendEmailThread(
                    request,
                    request.data['email'],
                    "registration",
                    Customer.objects.get(email=request.data['email']).verification_token
                ).start()
                return Response({"message": 'Email Verification sent!'}, status.HTTP_200_OK)
        if Customer.objects.filter(user_name=request.data['user_name']):
            return Response({"message": 'Username taken!'}, status.HTTP_200_OK)
        # if Customer.objects.filter(mobile_number=request.data['mobile_number']):
        #     return Response({"message": 'Mobile Number taken!'}, status.HTTP_200_OK)        
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            customer = serializer.save()
            SendEmailThread(
                request,
                request.data['email'],
                "registration",
                Customer.objects.get(email=request.data['email']).verification_token
            ).start()
            return Response({
                "status": status.HTTP_200_OK,
                "message": 'An Email has been sent to your email ID if it was valid.',
                "user": CustomerSerializer(customer, context=self.get_serializer_context()).data,
            })
        return Response({"Errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', 'GET'])
def verify(request, auth_token):
    try:
        customer = Customer.objects.filter(verification_token=auth_token).first()
        if customer:
            if customer.is_active:
                return Response({'message': "Your account is already verified."})
            customer.is_active = True
            customer.verification_token = None
            customer.save()
            # print(settings.SITE_URL)
            # return HttpResponse("<script>location.replace(settings.SITE_URL);</script>")
            # return redirect(settings.SITE_URL)
            return Response({'message': "Your account has now been verified."})
        else:
            return HttpResponse("Could not verify your registration.")
            # return Response({'message': "Could not verify your registration."})
    except Exception as e:
        return HttpResponse(e)
        # return Response({'message': e})

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def apply_for_verification(request):
    try:
        customer_images = CustomerImage.objects.get(customer=request.user)
        if customer_images:
            req, created = AdminPanelRequest.objects.get_or_create(
                customer=request.user, 
                req_type="Verification",
                img_1 = customer_images.img_1,
                img_2 = customer_images.img_2,
                img_3 = customer_images.img_3,
                img_4 = customer_images.img_4
                )
    except:
        req, created = AdminPanelRequest.objects.get_or_create(
                customer=request.user, 
                req_type="Verification"
                )
    if created:
        msg = "New request sent"
    else:
        msg = "Updated an existing response"
    return Response({"msg": msg, "data": AdminPanelRequesteSerializer(req).data})


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def user_details_edit(request):
    full_name = request.data.get('full_name')
    dob = request.data.get('dob')
    # mobile_number = request.data.get('mobile_number')
    about = request.data.get('about')
    i_am = request.data.get('i_am')
    looking_for = request.data.get('looking_for')
    city = request.data.get('city')
    country = request.data.get('country')
    age = request.data.get('age')
    hair_color = request.data.get('hair_color')
    weight = request.data.get('weight')
    sexual_orientation = request.data.get('sexual_orientation')
    languages = request.data.get('languages')
    height = request.data.get('height')
    img_1 = request.data.get('img_1')
    img_2 = request.data.get('img_2')
    img_3 = request.data.get('img_3')
    img_4 = request.data.get('img_4')
    try:
        # breakpoint()
        customer = Customer.objects.filter(user_name=request.user)
        if len(customer)==1:
            customer.update(
                full_name=full_name, about=about, dob=dob, i_am=i_am,
                looking_for=looking_for, city=city, country=country,
                age=age, hair_color=hair_color, weight=weight, height=height,
                sexual_orientation=sexual_orientation, languages=languages
            )
            customer[0].customerimage.img_1 = img_1
            customer[0].customerimage.img_2 = img_2
            customer[0].customerimage.img_3 = img_3
            customer[0].customerimage.img_4 = img_4
            customer[0].customerimage.save()
        return Response({"msg": "Account details edited.", 'new_data': CustomerSerializer(customer[0]).data})
    except:
        return Response({"msg": "Something Went Wrong"})


@api_view(['GET'])
def user_details(request):
    try:
        if request.user.is_authenticated == True:
            user_details = Customer.objects.get(email=request.user.email)
            serializer = CustomerSerializer(user_details)
            return Response({'user_details': serializer.data})
        else:
            return Response({'msg': "User not authenticated"})
    except:
        return Response({'msg': "something went wrong"})


@api_view(['POST'])
def change_password(request, token):
    try:
        customer = Customer.objects.filter(forget_password_token=token).first()
        if request.method == 'POST':
            new_password = request.data.get('new_password')
            confirm_password = request.data.get('confirm_password')
            parameter = request.data.get('email')
            if parameter is None:
                return Response({'message': 'Username/Email not relevant!'})
            if new_password != confirm_password:
                return Response({'message': 'New password does not match the confirm password field!'})
            if check_pass(new_password):
                try:
                    # try:
                    #     customer = Customer.objects.get(user_name=parameter)
                    # except:
                    #     customer = Customer.objects.get(email=parameter)
                    customer.set_password(new_password)
                    customer.forget_password_token = None
                    customer.save()
                    # messages.success(request, 'Password has been changed. Please log in through main website and close this tab!')
                    # return render(request, 'main/change_password.html')
                    return Response({'message': 'Password has been changed!'})
                except:
                    # return render(request, 'main/change_password.html', {'customer_id': customer.id})
                    return Response({'message': 'Password could not be changed! Error in Username/Email!'})
            else:
                return Response({'msg': 'Password should have minimun 6 characters and a number!'})
                # messages.success(request, 'Password should have minimun 6 characters and a number!')
                # return render(request, 'main/change_password.html', {'token': token})
        else:
            return Response({'msg': 'GET method not allowed'})
            # return render(request, 'main/change_password.html', {'customer_id': customer.id})
    except Exception as e:
        return Response({'msg': str(e)})
        # return HttpResponse("Some error occurred. Please contact us from the main website.")


@api_view(['POST'])
def forgot_password(request):
    try:
        parameter = request.data.get('email')
        try:
            try:
                customer = Customer.objects.get(email=parameter)
            except:
                customer = Customer.objects.get(user_name=parameter)
            while True:
                token = str(uuid.uuid4())
                if not Customer.objects.filter(forget_password_token=token).first():
                    break
            customer.forget_password_token = token
            customer.save()
            SendEmailThread(
                request,
                request.data['email'],
                "password_reset",
                token
                # Customer.objects.get(email=request.data['email']).verification_token
            ).start()
            # send_email_for_password_reset(request.get_host(), customer.email, customer.forget_password_token)
            return Response({'message': "An email is sent to your email id"})
        except:
            return Response({'message': "No User found with this username or email"})
    except Exception as e:
        return Response({'message': e})
