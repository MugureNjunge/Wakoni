from rest_framework import serializers
from .models import Profile, Locality

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=('fullname','bio','profile_pic','user','locality')

class LocalitySerializer(serializers.ModelSerializer):
    class Meta:
        model=Locality
        fields=('locality_name','occupants','locality_image')        