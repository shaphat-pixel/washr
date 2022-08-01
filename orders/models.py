from time import time
from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL
import geocoder
# Create your models here.


mapbox_access_token = 'pk.eyJ1Ijoic2hhcGhhdCIsImEiOiJjbDJhd3NmazUwOXFyM2VwZXo2YjQwdGFpIn0.NZ1wB_nlY35DxeeGbyNsVg'

class Orders(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shirts = models.IntegerField()
    shorts = models.IntegerField()
    trousers = models.IntegerField()

    total_units = models.CharField(max_length=2000, blank=True)

    shirts_amount = models.CharField(max_length=2000, blank=True)
    shorts_amount = models.CharField(max_length=2000, blank=True)
    trousers_amount = models.CharField(max_length=2000, blank=True)

    total = models.CharField(max_length=2000,blank=True)

    verified = models.BooleanField(null=True)
    doing_laundry = models.BooleanField(null=True)
    delivery_underway = models.BooleanField(null=True)
    delivered = models.BooleanField(null=True)

    address = models.TextField(default='')

    time = models.DateTimeField(auto_now=True)

    #lat = models.FloatField(blank=True)
    #long = models.FloatField(blank=True)
    #image = models.CharField(max_length=200)


    def shirts_total_amount(self):
        shirts = self.shirts
        total = (shirts) * 3

        return total

    def shorts_total_amount(self):
        shorts = self.shorts
        total = (shorts) * 2

        return total

    def trousers_total_amount(self):
        trousers = self.trousers
        total = (trousers) * 5

        return total


    def unit_sum(self):
        shorts = self.shorts
        shirts = self.shirts
        trousers = self.trousers
        total = shorts + shirts + trousers

        return total

    def total_amount(self):
        shorts = self.shorts
        shirts = self.shirts
        trousers = self.trousers
        total = (shirts)*3 + (shorts)*2 + (trousers)*5

        return total

    def save(self, *args, **kwargs):
        self.total = str(self.total_amount())
        self.total_units = str(self.unit_sum())
        self.shirts_amount = str(self.shirts_total_amount())
        self.shorts_amount = str(self.shorts_total_amount())
        self.trousers_amount = str(self.trousers_total_amount())

        #g = geocoder.mapbox(self.address, key=mapbox_access_token)
        #g = g.latlng  # returns     => [lat, long]
        #self.lat = g[0]
        #self.long = g[1]

        super().save(*args, **kwargs)


    def __str__(self):
        return f'{self.user.username} Orders'