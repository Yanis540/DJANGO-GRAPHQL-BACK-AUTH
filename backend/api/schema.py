from graphene import ObjectType,Schema,Field,String

from .Types.types import UserType
from djongo.models.fields import ObjectId
from .models import User
class RootQuery(ObjectType):
    name=Field(UserType)
    def resolve_name(parent,info):
        user=User.objects.get(_id=ObjectId('620bac44906d196bcfb5b2cd'))
        return user


schema=Schema(query=RootQuery)