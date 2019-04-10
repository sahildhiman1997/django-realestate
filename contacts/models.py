from django.db import models
from datetime import datetime
from django.core.validators import MaxValueValidator 
# Create your models here.
class Contact(models.Model):
    listing=models.CharField(max_length=200)
    listing_id=models.IntegerField()
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=200)
    phone=models.BigIntegerField(validators=[MaxValueValidator(9999999999)])
    message=models.TextField(blank=True)
    dated=models.DateTimeField(default=datetime.now, blank=True)
    user_id=models.IntegerField(blank=True)
    def __str__(self):
        return self.name