from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter
from schema.schema import UserCreateSchema
from db.db_connect import get_db
from sqlalchemy.orm import Session
from db.models import User
from utils.passwordUtils import hash

router = APIRouter()
@router.post('/user/create/',status_code=status.HTTP_201_CREATED)
def userCreate(request:UserCreateSchema,db:Session = Depends(get_db)):
    hashed_pass = hash(request.password)
    request.password = hashed_pass
    user = User(**request.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return {'status':'created','info':{"email":user.email,'password':user.password,'created':user.created_at}}

@router.get('/user/info/{id}/',status_code=status.HTTP_200_OK)
def userInfo(id:int,db:Session = Depends(get_db)):
    user = db.query(User).filter(User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No Such User")
    return {'user':user.email}
