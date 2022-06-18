from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.dispatch import receiver


class Profile(models.Model):
    
    user = models.OneToOneField(User,on_delete=models.CASCADE, null=True)
    fullname = models.CharField(max_length=50,blank=True)
    locality = models.CharField(max_length=30, blank=True, null=True)
    profile_pic= CloudinaryField('image')
    bio= models.CharField(max_length=50,blank=True)
    email= models.EmailField(max_length=50,blank=True)

    def __str__(self):
        return self.fullname

    @classmethod
    def save_profile(self):
      self.save() 

    def search_profile(cls, name):
        profile = Profile.objects.filter(user__username__icontains = name)
        return profile

    def update_profile(self):
         self.update()        

    def delete_profile(self):
         self.delete()

class Locality(models.Model):

    locality_name = models.CharField(max_length=30)
    occupants = models.IntegerField(blank=True, null=True)
    locality_image= CloudinaryField('image')
   
    user= models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.location + ' - ' + self.locality_name
    
    def create_locality(self):
        self.create()

    @classmethod
    def search_by_localities(cls, search_term):
        localities = cls.objects.filter(title__icontains=search_term)
        return localities  

    def update_locality(self):
       self.update()    

    def update_occupants(self):
       self.update()        
       
    def delete_locality(self):
        self.delete()         

class Post(models.Model):
    title= models.CharField(max_length=100)
    post_image= CloudinaryField('image')
    description= models.TextField()
    
    user= models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    

    def __str__(self):
        return self.title + ' - ' + self.description
    
    def save_post(self):
        self.save()

    def delete_post(self):
       self.delete()    

    @classmethod
    def search_by_posts(cls, search_term):
        posts = cls.objects.filter(title__icontains=search_term)
        return posts    

    @classmethod
    def get_posts_by_profile(cls, profile):
        posts = Post.objects.filter(profile__pk=profile)
        return posts





    

