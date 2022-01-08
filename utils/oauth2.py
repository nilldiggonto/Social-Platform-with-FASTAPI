from jose import JWTError,jwt
from datetime import datetime,timedelta

from sqlalchemy.orm.session import Session
from schema.schema import TokenDataSchema
from fastapi import Depends,status,HTTPException
from fastapi.security import OAuth2PasswordBearer
from db.db_connect import get_db
from db.models import User
from config.config import settings


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
#SECRET KEY FOR CHECK
# python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES =settings.ACCESS_TOKEN_EXPIRE_MINUTES

def create_access_token(data:dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    encoded_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt


#--verify token
def verfiyAccessToken(token:str,credentials_exception):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        id:str  = payload.get("user_id")
        if id is None:
            raise credentials_exception
        token_data =    TokenDataSchema(id=id)
    except JWTError:
        raise credentials_exception
    return token_data

def get_user(token:str = Depends(oauth2_scheme),db:Session=Depends(get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Jwt Validation Failed",headers={"WWW-Authenticate":"Bearer"})
    token = verfiyAccessToken(token,credentials_exception) 
    user = db.query(User).filter(User.id == token.id).first()
    return user



