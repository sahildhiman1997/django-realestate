from django.db import models
from datetime import datetime
from realtors.models import Realtor
# Create your models here.
class Listing(models.Model):
    realtor=models.ForeignKey(Realtor,on_delete=models.DO_NOTHING)
    title=models.CharField(max_length=200)
    address=models.CharField(max_length=400)
    city=models.CharField(max_length=50)
    pincode=models.CharField(max_length=200)
    description=models.TextField(blank=True)
    price=models.IntegerField()
    bedrooms=models.IntegerField()
    bathrooms=models.DecimalField(max_digits=2, decimal_places=1)
    sqft=models.IntegerField()
    photommain=models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo1=models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo2=models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo3=models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo4=models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo5 =models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    published=models.BooleanField(default=True)
    dated=models.DateTimeField(default=datetime.now,blank=True)
    def __str__(self):
        return self.title