from django.http import  JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import User 
from .seriliazers import UserSerializer
# Create your views here.
@api_view(['GET'])
def test(req):
    users_unserialized=User.objects.all()
    users_serialized=UserSerializer(users_unserialized,many=True)
    users=users_serialized.data
    return JsonResponse(users,safe=False)