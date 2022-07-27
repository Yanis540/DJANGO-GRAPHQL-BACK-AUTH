from api.Types.types import UserType 
from graphene import ObjectType,List,Field,ID
from api.models import User
from djongo.models.fields import ObjectId

class QueryUser(ObjectType):
    users=List(UserType)
    user=Field(UserType,args={
        'id':ID(required=True)
    })
    
    #add the middlewares
    def resolve_users(parent,info):
        try: 
            return User.objects.all()
        except Exception as e : 
            raise Exception(str(e))

    def resolve_user(parent,info,id):
        try: 
            return User.objects.get(_id=ObjectId(id))
        except Exception as e : 
            raise Exception(str(e))        
    