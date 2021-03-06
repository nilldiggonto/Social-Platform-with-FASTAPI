from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from db.db_connect import Base
from sqlalchemy import Column,String,Integer,Boolean
from sqlalchemy.sql.sqltypes import TIME, TIMESTAMP
from sqlalchemy.sql.expression import column, null, text

class Post(Base):
    __tablename__ = 'posts'

    id      =   Column(Integer,primary_key=True,nullable=False)
    title   =   Column(String,nullable=False)
    content =   Column(String,nullable=False)
    publish =   Column(Boolean,server_default="True",nullable=False)
    created_at  =  Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    owner_id   =   Column(Integer,ForeignKey('users.id',ondelete="CASCADE"),nullable=False)
    owner   =   relationship("User") 

#----------- USER MODEL
class User(Base):
    __tablename__ = 'users'
    id          =   Column(Integer,primary_key=True,nullable=False)
    phone_no    =   Column(String,nullable=True)
    email       =   Column(String,nullable=False,unique=True)
    password    =   Column(String,nullable=False)
    created_at  =   Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))

#--- RATING SYSTEM
class Rate(Base):
    __tablename__ = 'rates'
    
    user_id     =   Column(Integer,ForeignKey('users.id',ondelete="CASCADE"),primary_key=True)
    post_id     =   Column(Integer,ForeignKey('posts.id',ondelete="CASCADE"))
    

