from typing import Optional
from pydantic import BaseModel

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

