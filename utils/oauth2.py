from jose import JWTError,jwt
from datetime import datetime,timedelta
from schema.schema import TokenDataSchema
from fastapi import Depends,status,HTTPException
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
#SECRET KEY FOR CHECK
# python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

SECRET_KEY = "i@+ms60tfhs^xfdal_vyp40l^xb8&z)r+cbfwgzr!s_3g3d3bf"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

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

def get_user(token:str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Jwt Validation Failed",headers={"WWW-Authenticate":"Bearer"})
    return verfiyAccessToken(token,credentials_exception)



