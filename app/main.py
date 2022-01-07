from os import stat
from fastapi import FastAPI,Response,status,HTTPException,Depends
from fastapi.param_functions import Body
from schema.schema import PostSchema
from db.models import Post
from db.db_connect import Base,engine,get_db
from sqlalchemy.orm import Session

#Testing
# from random import randrange

app  = FastAPI()

#Dummy Data
dummy_data = [
    {"title":"FastAPI","content":"This is fast","id":1},
    {"title":"Django","content":"This is for large application","id":2},
]

#_____________
#
#CREATING DB
#______________
Base.metadata.create_all(bind=engine)



#----------initial
@app.get('/')
def root():
    return {'info':'yo fastapi'}

#--Getting posts
@app.get('/posts')
def all_posts(db:Session = Depends(get_db)):
    posts = db.query(Post).all()
    print(posts)
    return {'status':'success','info':posts}

#--creating posts without schema
@app.post('/create/post')
def create_post(request: dict= Body(...)):
    title = request['title']
    return {'status':'success','info':{'title':title}}

#--creating post with schema
@app.post('/create/post/s/',status_code=status.HTTP_201_CREATED)
def create_postSchema(request:PostSchema,db:Session=Depends(get_db)):
    # data = request.dict() 
    new_post = Post(**request.dict() ) #fastest
    # new_post = Post(title= request.title,content=request.content,publish=request.publish)#morecode
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {'status':'success','info':new_post}


#Fetching single post
@app.get("/post/{id}")
def blogSingle(id:int,db:Session=Depends(get_db)):
    blog = db.query(Post).filter(Post.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='no such query found')
    return {'status':'success','info':blog}
#update post
@app.put('/post/update/{id}')
def updatePost(id:int,request:PostSchema,db:Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id==id)
    post_edit = post.first()
    if not post_edit:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='no such query found')
    post.update(request.dict(),synchronize_session=False)
    db.commit()
    return {'status':'success','data':post.first()}

#Delete Post
@app.delete('/post/delete/{id}',status_code=status.HTTP_204_NO_CONTENT)
def deletePost(id:int,db:Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id==id)
    print(post)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='no such query found')
    post.delete(synchronize_session=False)
    db.commit()
    return {'status':'deleted'}


#For refrence fetching single id
"""@app.get("/post/{id}")
def blogSingle(id:int,db:Session=Depends(get_db)):
#def blogSingle(id:int,response:Response):
    db.query(Post).filter(Post.id==id).first()
    data = {'id':id}
    #
    # response.status_code = 404
    # response.status_code = 200
    # response.status_code = "Any Valid Http code"
    # response.status_code = status.HTTP_200_OK
    #---no need to pass responseResponse
    # raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,detail=data)
    return {'status':'success','info':data}"""

