from django.db import models
from datetime import datetime
from django.core.validators import MaxValueValidator


# Create your models here.
class Realtor(models.Model):
    name=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='photos/realtors')
    description=models.TextField(blank=True)
    phone=models.IntegerField(validators=[MaxValueValidator(999999999999)])
    ismvp=models.BooleanField(default=False)
    email=models.EmailField(max_length=254,default='none@none.com')
    hireddate=models.DateField(default=datetime.now,blank=True)
    def __str__(self):
        return self.name