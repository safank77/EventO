from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Event(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='event_images')
    description=models.CharField(max_length=500)
    options=(
        ('DJ Party','DJ Party'),
        ('Marriage Function','Marriage Function'),
        ('Conference Event','Conference Event'),
        ('Academic Event','Academic Event'),
        ('Customized Event','Customized Event')
    )



class Book(models.Model):
    event=models.ForeignKey(Event,on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    phone=models.IntegerField(null=True)
    address=models.CharField(max_length=500,null=True)
    date=models.DateField(null=True)
    time=models.TimeField(null=True)
    description=models.CharField(max_length=500,null=True)
    options=(
        ('Booking Confirmed','Booking Confirmed'),
        ('Cancelled','Cancelled')
    )
    status=models.CharField(max_length=100,choices=options,default='Booking Confirmed')

    

