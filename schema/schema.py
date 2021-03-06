from typing import Optional
from pydantic import BaseModel,EmailStr
from datetime import datetime

from pydantic.types import conint

# from db.db_connect import Base
#

#BASE POST SCHEMA
class PostBaseSchema(BaseModel):
    title       :   str
    content     :   str
    publish     :   bool    =   True

#FETCHING POST SCHEMA
class PostSchema(BaseModel):
    title   :   str
    content :   str
    publish :   bool    =   True
    
    # rating  :   Optional[int]   =   None


#CREATING POST SCHEMA
class CreatePostSchema(PostBaseSchema):
    pass


# #UPDATE POST SCHEMA
# class UpdatePostSchema(PostBaseSchema):
#     pass

#-------------RESPONSE SCHEMA
class PostResponseSchema(PostBaseSchema):
    created_at  :   datetime
    class Config:
        orm_mode = True


    #---------------
#--------User
class UserCreateSchema(BaseModel):
    email       :   EmailStr
    password    :   str

#-----login
class UserLoginSchema(BaseModel):
    email       :   EmailStr
    password    :   str

#--send token schema
class TokenSchema(BaseModel):
    access_token    :   str
    token_type      :   str

class TokenDataSchema(BaseModel):
    id  :   Optional[str]   =   None


#--Rating Schema
class RateSchema(BaseModel):
    post_id     :   int
    rate        :   bool
