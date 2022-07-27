from api.Types.types import AuthType 
from graphene import ObjectType, Field,String 
from api.models import User 
from api.seriliazers import UserSerializer
from django.contrib.auth.hashers import check_password,make_password
from api.tokens import create_auth_token
class UserMutation(ObjectType):
    login=Field(AuthType,args={
        'email':String(required=True),
        'password':String(required=True),
    })
    
    def resolve_login(parent,info,email,password):
        try:
            user_unserialized=User.objects.get(email=email)
            user_serialized=UserSerializer(user_unserialized)
            user=user_serialized.data
            if not check_password(password,user['password']):raise Exception('Invalid Password')
            authInfos=create_auth_token(user['_id'])
            accessToken=authInfos['accessToken']
            refreshToken=authInfos['refreshToken']
            expiresIn=authInfos['expiresIn']
            return{
                'user':user_unserialized,
                'accessToken':accessToken,
                'refreshToken':refreshToken,
                'expiresIn':expiresIn
            }
        except Exception as e: 
            raise Exception(e)