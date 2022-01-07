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


#----------- USER MODEL
class User(Base):
    __tablename__ = 'users'
    id          =   Column(Integer,primary_key=True,nullable=False)
    email       =   Column(String,nullable=False,unique=True)
    password    =   Column(String,nullable=False)
    created_at  =   Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))

