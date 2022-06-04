from distutils.command.upload import upload
from email.headerregistry import Address
from pickle import TRUE
from django.db import models
from django.utils import timezone
import math
from django.forms import DateTimeField

# Create your models here.
class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=40)
    phone = models.CharField(max_length=15)
    is_activate = models.BooleanField(default=True)
    is_verify = models.BooleanField(default=False)
    role = models.CharField(max_length=40)
    create_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.email

class Ngo(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=40,blank=True,null=True)        
    # email = models.EmailField(unique=True)
    role = models.CharField(max_length=40,blank=True,null=True)
    contact_person_number = models.CharField(max_length=15,blank=True,null=True)
    contact_person_name = models.CharField(max_length=40,blank=True,null=True)
    registration_no = models.CharField(max_length=50,blank=True,null=True)
    no_member = models.IntegerField(blank=True,null=True)
    working_hourse = models.CharField(max_length=40,blank=True,null=True)
    city = models.CharField(max_length=40,blank=True,null=True)
    locations = models.CharField(max_length=40,blank=True,null=True)
    address = models.TextField(max_length=300,blank=True,null=True)
    about_us = models.TextField(max_length=600,blank=True,null=True)
    logo = models.FileField(upload_to='media/images/',default='media/tiger.jpg')

    def __str__(self):
        return self.name

class Customer(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    contact_number = models.CharField(max_length=15)
    city = models.CharField(max_length=30)
    Address = models.CharField(max_length=200,blank = True)
    rewards_points = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class FoodPickup(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    food_quality = models.CharField(max_length=30,blank=True,null=True)       
    food_category = models.CharField(max_length=50,blank=True,null=True)
    food_description = models.TextField()
    pick_up_location = models.CharField(max_length=50,default="",blank=True,null=True)
    
    food_donor_purpose = models.CharField(max_length=20,default="",blank=True,null=True)
    pick_up_address = models.TextField(default="")
    pick_up_time = models.IntegerField()
    food_status = models.CharField(max_length=50,blank=True,null=True)
    picture = models.FileField(upload_to='media/images/',default='media/food-defualt.jpg')
    create_at = models.DateTimeField(auto_now_add = True,blank = False)
    update_at = models.DateTimeField(auto_now = True,blank=False)

    def __str__(self):
        return self.food_category

    def whenpublished(self):
        now = timezone.now()

        diff=now - self.create_at

        if diff.days==0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds = diff.seconds

            if seconds == 1:
                return str(seconds) + "second ago"

            else:
                return str(seconds) + "seconds ago"
        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes = math.floor(diff.seconds/60)

            if minutes == 1:
                return str(minutes) + " minute ago" 
            else:
                return str(minutes) + " minutes ago"
        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            minutes = math.floor(diff.seconds/3600)

            if minutes == 1:
                return str(minutes) + " day ago" 
            else:
                self.food_status = "Expired"
                self.save()
                return str(minutes) + " days ago"
        if diff.days == 0 and diff.seconds >= 86400 and diff.seconds < 3156420:
            minutes = math.floor(diff.seconds/60)

            if minutes == 1:
                return str(minutes) + " month ago" 
            else:
                return str(minutes) + " month's ago"
         
class POST_NGO(models.Model):
    Ngo_id = models.ForeignKey(Ngo,on_delete=models.CASCADE)
    title = models.CharField(max_length=30)         
    description = models.TextField()
    likes = models.IntegerField()
    views = models.IntegerField()
    picture = models.FileField(upload_to='media/images/',default='media/food-defualt.jpg',blank=True,null=True)
    videofile = models.FileField(upload_to = 'videos/', null=True,verbose_name="",blank = True)
    audiofile = models.FileField(upload_to = 'media/musics/',null=True)
    create_at = models.DateTimeField(auto_now_add = True,blank = False)
    update_at = models.DateTimeField(auto_now = True,blank=False)


    def __str__(self):
        return self.title