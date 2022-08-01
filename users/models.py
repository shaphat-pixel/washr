from django.conf import settings
User = settings.AUTH_USER_MODEL
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import UserManager
from orders.models import Orders


from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail 
# Create your models here.


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=100)
    
    
@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=100, default="")
    email = models.CharField(max_length=100, default="")
    


    def save(self, *args, **kwargs):
        self.id = self.user.id
        self.username = self.user.username
        self.email = self.user.email
        

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.user.username} Profile'

class User_Order(models.Model):
    order = models.OneToOneField(Orders, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    shirts = models.IntegerField(default=0)
    shorts = models.IntegerField(default=0)
    trousers = models.IntegerField(default=0)

    total_units = models.CharField(max_length=2000, blank=True)
    
    shirts_amount = models.CharField(max_length=2000, blank=True)
    shorts_amount = models.CharField(max_length=2000, blank=True)
    trousers_amount = models.CharField(max_length=2000, blank=True)
    
    total = models.CharField(max_length=200,blank=True)
    
    

    verified = models.BooleanField(null=True)
    doing_laundry = models.BooleanField(null=True)
    delivery_underway = models.BooleanField(null=True)
    delivered = models.BooleanField(null=True)

    address = models.TextField(default='')

    time = models.DateTimeField(auto_now=True)
    
    
    def save(self, *args, **kwargs):
        self.user = self.order.user
        self.id = self.order.id
        self.shirts = self.order.shirts
        self.shorts = self.order.shorts
        self.trousers = self.order.trousers
        self.total_units = self.order.total_units
        self.shirts_amount = self.order.shirts_amount
        self.shorts_amount = self.order.shorts_amount
        self.trousers_amount = self.order.trousers_amount
        self.total = self.order.total
        self.verified = self.order.verified
        self.doing_laundry = self.order.doing_laundry
        self.delivery_underway = self.order.delivery_underway
        self.delivered = self.order.delivered
        self.address = self.order.address

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.order.user.username} Order'

    
