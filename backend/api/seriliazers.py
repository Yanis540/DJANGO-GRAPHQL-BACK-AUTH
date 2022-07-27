from rest_framework import serializers
from .models import User
from djongo.models.fields import ObjectIdField
class UserSerializer(serializers.ModelSerializer):
    _id=ObjectIdField()
    class Meta: 
        model=User  
        fields='__all__'
        