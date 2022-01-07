from os import access
from fastapi import FastAPI,APIRouter,Depends,status,HTTPException
from sqlalchemy.orm import Session
from db.db_connect import get_db
from schema.schema import UserLoginSchema
from db.models import User
from utils.passwordUtils import verifyPass
from utils.oauth2 import create_access_token
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

router = APIRouter(
    tags = ['Authentication']
)

@router.post('/login')
def userLogin(request:UserLoginSchema, db:Session = Depends(get_db)):
    user = db.query(User).filter(User.email== request.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid Credentials")
    if not verifyPass(request.password,user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid Credentials")

    access_token = create_access_token(data= {"user_id":user.id})

    return {"access_token":access_token,"token_type":"bearer"}

######
#
# Built-In FastAPI OauthForm
#
#####
# @router.post('/login')
# def userLogin(request:OAuth2PasswordRequestForm = Depends(), db:Session = Depends(get_db)):
#     user = db.query(User).filter(User.email== request.username).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Invalid Credentials")
#     if not verifyPass(request.password,user.password):
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Invalid Credentials")

#     access_token = create_access_token(data= {"user_id":user.id})

#     return {"access_token":access_token,"token_type":"bearer"}


