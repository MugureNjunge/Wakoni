from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.dispatch import receiver


class Profile(models.Model):
    
    user = models.OneToOneField(User,on_delete=models.CASCADE, null=True)
    fullname = models.CharField(max_length=100,blank=True)
    locality = models.CharField(max_length=200, blank=True, null=True)
    lane_number = models.IntegerField(blank=True, null=True)
    profile_pic= CloudinaryField('image')

    def __str__(self):
        return self.fullname

    @classmethod
    def save_profile(self):
      self.save() 

    def search_profile(cls, name):
        profile = Profile.objects.filter(user__username__icontains = name)
        return profile

    def delete_profile(self):
         self.delete()

class Locality(models.Model):
    name = models.CharField()
    location= models.CharField()
    occupants = models.IntegerField(blank=True, null=True)
   
    user= models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title + '' + self.description
    
    def save_locality(self):
        self.save()

    @classmethod
    def search_by_localities(cls, search_term):
        localities = cls.objects.filter(title__icontains=search_term)
        return localities

    @classmethod
    def search_by_user(cls, user):
        localities = cls.objects.filter(user=user)
        return localities     

    def delete_locality(self):
        self.delete()         

  

