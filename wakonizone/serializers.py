from rest_framework import serializers
from .models import Profile, Locality, Business, Post

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=('fullname','bio','profile_pic','user','locality')

class LocalitySerializer(serializers.ModelSerializer):
    class Meta:
        model=Locality
        fields=('locality_name','occupants','location')        

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model=Business
        fields=('title','description','business_image','link','business_email')   

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=('title','description','post_image')                       