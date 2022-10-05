from django.db.models.signals import post_save, pre_save
from .models import Customer, AdminPanelRequest

def create_publish_request(sender, instance, **kwargs):
    # breakpoint()
    req = AdminPanelRequest.objects.create(
        customer=instance, 
        img_1=instance.get_image_url[0].img_1,
        img_2=instance.get_image_url[0].img_2,
        img_3=instance.get_image_url[0].img_3,
        img_4=instance.get_image_url[0].img_4,
        )

# def update_customer(sender, instance, **kwargs):
    

# pre_save(update_customer, sender=AdminPanelRequest)

post_save.connect(create_publish_request, sender=Customer)