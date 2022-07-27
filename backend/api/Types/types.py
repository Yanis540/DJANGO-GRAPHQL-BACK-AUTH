from graphene import String,ObjectType,Field,Int
from graphene_django import DjangoObjectType
from graphene_django.converter import convert_django_field
from djongo.models.fields import ObjectIdField,ObjectId,ForeignKey
from api.models import User
@convert_django_field.register(ObjectIdField)
def convert_ObjectIdField(field, registry=None):
    return String()
@convert_django_field.register(ForeignKey)
def convert_ForeignKey(field, registry=None):
    return String()


class UserType(DjangoObjectType):
    _id=ObjectIdField()
    class Meta: 
        model=User 
        fields=('_id','email','name')
        
class AuthType(ObjectType):
    user=Field(UserType)
    accessToken=String()
    refreshToken=String()
    expiresIn=Int()
    class Meta: 
        model=User 
        fields='__all__'