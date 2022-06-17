from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.dispatch import receiver


class Profile(models.Model):
    
    user = models.OneToOneField(User,on_delete=models.CASCADE, null=True)
    fullname = models.CharField(max_length=100,blank=True)
    locality = models.CharField(max_length=200, blank=True, null=True)
    locale_lane = models.CharField(max_length=200, blank=True, null=True)
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

  

