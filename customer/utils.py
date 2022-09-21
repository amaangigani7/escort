from django.core.mail import send_mail
from django.conf import settings
import threading
from threading import Thread
from .models import *
import asyncio
import time

class SendEmailThread(threading.Thread):

    def __init__(self, request, email, e_type, token=None, current_time=None):
        self.request = request
        self.email = email
        self.token = token
        self.e_type = e_type
        self.current_time = time.time()
        threading.Thread.__init__(self)

    def run(self):
        if self.e_type == "registration":
            try:
                subject = "Email verification"
                text = "Hi, This is the link to verify you registration email with our site {0}. Please paste the link to verify your account {0}/auth/verify/{1}/"
                message = text.format(self.request.get_host(), self.token)
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [self.email,]
                send_mail(subject, message, email_from, recipient_list)
            except Exception as e:
                print("{} :- ".format(self.email), e)
        elif self.e_type == "password_reset":
            try:
                subject = 'Reset your password here'
                message = 'Hi, click on the link to reset your password {}/auth/change_password/{}'.format(self.request.get_host(), self.token)
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [self.email,]
                send_mail(subject, message, email_from, recipient_list)
                print("sent")
            except Exception as e:
                print("{} :- ".format(self.email), e)

    # def send_email_for_password_reset(self):
    #     subject = 'Reset your password here'
    #     message = 'Hi, click on the link to reset your password {}/main/change_password/{}'.format(self.host, self.token)
    #     email_from = settings.EMAIL_HOST_USER
    #     recipient_list = [self.email,]
    #     # send_mail(subject, message, email_from, recipient_list)
    #     print("sent this one two")


def check_pass(new_password):
    check_len, check_num, check_alpha = False, False, False
    for i in new_password:
        if check_num == False:
            if i.isdigit():
                check_num = True
            elif i.isalpha():
                check_alpha = True
    if 16 >= len(new_password) >= 6:
        check_len = True
    if check_len == True and check_num == True and check_alpha == True:
        return True
    else:
        return False


def send_email_after_registration(request, email, token):
    # email_data_list = EmailData.objects.filter(title='Registration')
    # email_data = email_data_list[0]
    # if len(email_data_list) == 1:
    try:
        subject = "Email verification"
        text = "Hi, This is the link to verify you registration email with our site {0}. Please paste the link to verify your account {0}/auth/verify/{1}/"
        message = text.format(request.get_host(), token)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email,]
        send_mail(subject, message, email_from, recipient_list)
        print("sent")
        return "success"
    except:
        return "fail"
    
    # else:
    #     print('Could not find the text to send email.')


# def send_email_for_password_reset(host, email, token):
#     subject = 'Reset your password here'
#     message = 'Hi, click on the link to reset your password {}/main/change_password/{}'.format(host, token)
#     email_from = settings.EMAIL_HOST_USER
#     recipient_list = [email,]
#     send_mail(subject, message, email_from, recipient_list)
