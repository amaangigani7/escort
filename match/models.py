from django.db import models
from customer.models import *

# Create your models here.
class Like(models.Model):
    sender = models.ForeignKey(Customer, related_name="sender", on_delete=models.SET_NULL, null=True)
    to = models.ForeignKey(Customer, related_name="receiver_liked", on_delete=models.SET_NULL, null=True)
    # receiver = models.ManyToManyField(Customer, related_name="receiver_liked")
    liked_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    read = models.BooleanField(default=False)
    # match = models.BooleanField(default=False)

    # def save(self, *args, **kwargs):
    #     already = self.__class__.objects.filter(sender=self.to, to=self.sender)
    #     if len(already) >= 1:
    #         self.match = True
    #     super().save(*args, **kwargs)


    def __str__(self):
        return "{} liked {}".format(self.sender.user_name, self.to.user_name)

class Review(models.Model):
    sender = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    to = models.ForeignKey(Customer, related_name="receiver_reviewed", on_delete=models.SET_NULL, null=True)
    content = models.TextField(null=True)
    sent_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    read = models.BooleanField(default=False)
    # match = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        already = self.objects.filter(sender=self.to, to=self.sender)
        if len(already) >= 1:
            self.match = True
        super().save(*args, **kwargs)

    def __str__(self):
        return "{} to {} : {}".format(self.sender.user_name, self.to.user_name, self.content)