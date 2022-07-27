import jwt 
from datetime import datetime
import time  
from backend.settings import ACCESS_TOKEN_SECRET,REFRESH_TOKEN_SECRET

def generatre_access_token(id):
    expiresIn=int (time.time() +3600 )
    token=jwt.encode({
        'id':id,
        'exp':expiresIn
    },ACCESS_TOKEN_SECRET,algorithm='HS256')
    return {
        'accessToken':token.decode('utf-8'),
        'expiresIn':expiresIn
    }
def generatre_refresh_token(id):
    expiresIn=int (time.time() +24*3600 )
    token=jwt.encode({
        'id':id,
        'exp':expiresIn
    },ACCESS_TOKEN_SECRET,algorithm='HS256')
    return token.decode('utf-8')

def create_auth_token(id):
    accessTokenElement=generatre_access_token(id)
    refreshToken=generatre_refresh_token(id)
    accessToken=accessTokenElement['accessToken']
    expiresIn=accessTokenElement['expiresIn']
    return {
        'accessToken':accessToken,
        'expiresIn':expiresIn,
        'refreshToken':refreshToken
    }
