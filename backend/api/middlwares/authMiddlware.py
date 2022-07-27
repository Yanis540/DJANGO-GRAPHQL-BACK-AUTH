import jwt 
from backend.settings import ACCESS_TOKEN_SECRET,REFRESH_TOKEN_SECRET 
from api.models import User
from djongo.models.fields import ObjectId

def login_required(func):
    def login_wrapper(parent,info,**args):
        try:
            req=info.context 
            if (not req.headers or not req.headers['Authorization'] or not req.headers['Authorization'].startswith('Bearer')) : raise Exception('Unauthorized')
            token=req.headers['Authorization'] .split(' ')[1]
            decode=jwt.decode(token,ACCESS_TOKEN_SECRET,algorithms='HS256')
            user=User.objects.get(_id=ObjectId(decode['id']))
            info.context.user=user 
            return func(parent,info,**args)
        except Exception as e: 
            raise Exception(e)
        
    return login_wrapper
def refresh_middlware(func):
    def login_wrapper(parent,info,**args):
        try:
            req=info.context 
            if (not req.headers or not req.headers['Authorization'] or not req.headers['Authorization'].startswith('Bearer')) : raise Exception('Unauthorized')
            token=req.headers['Authorization'] .split(' ')[1]
            decode=jwt.decode(token,REFRESH_TOKEN_SECRET,algorithms='HS256')
            user=User.objects.get(_id=ObjectId(decode['id']))
            info.context.user=user 
            return func(parent,info,**args)
        except Exception as e: 
            raise Exception(e)
        
    return login_wrapper