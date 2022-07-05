from rest_framework import serializers
from rmc.models import User, Professional, Session
from rmc.validators import *

class UserSerializer (serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('user_name','email','password','is_active')
        extra_kwargs = {'password': {'write_only': True}}

class ProfessionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professional
        fields = '__all__'
        

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        exclude = []
