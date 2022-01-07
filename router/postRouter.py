from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter
from schema.schema import PostResponseSchema,CreatePostSchema
from db.db_connect import get_db
from sqlalchemy.orm import Session
from db.models import Post
from typing import List
from fastapi.param_functions import Body

router = APIRouter()


@router.get('/posts',response_model= List[PostResponseSchema] )
def all_posts(db:Session = Depends(get_db)):
    posts = db.query(Post).all()
    return posts
    # return posts

#--creating posts without schema
@router.post('/create/post')
def create_post(request: dict= Body(...)):
    title = request['title']
    return {'status':'success','info':{'title':title}}

#--creating post with schema
@router.post('/create/post/s/',status_code=status.HTTP_201_CREATED)
def create_postSchema(request:CreatePostSchema,db:Session=Depends(get_db)):
    # data = request.dict() 
    new_post = Post(**request.dict() ) #fastest
    # new_post = Post(title= request.title,content=request.content,publish=request.publish)#morecode
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {'status':'created','data':{'title':new_post.title,'content':new_post.content}}


#Fetching single post
@router.get("/post/{id}")
def postSingle(id:int,db:Session=Depends(get_db)):
    post = db.query(Post).filter(Post.id==id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='no such query found')
    return {'status':'success','post':{'title':post.title,'content':post.content}}
#update post
@router.put('/post/update/{id}')
def updatePost(id:int,request:CreatePostSchema,db:Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id==id)
    post_edit = post.first()
    if not post_edit:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='no such query found')
    post.update(request.dict(),synchronize_session=False)
    db.commit()
    return {'status':'success','data':post.first()}

#Delete Post
@router.delete('/post/delete/{id}',status_code=status.HTTP_204_NO_CONTENT)
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

