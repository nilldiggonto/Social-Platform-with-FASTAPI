
from fastapi import FastAPI
from db.db_connect import Base,engine
from router import postRouter,userRouter

app  = FastAPI()
#_____________
#
#CREATING DB
#______________
Base.metadata.create_all(bind=engine)
#----------initial
@app.get('/')
def root():
    return {'info':'yo fastapi'}
#---post-routes
app.include_router(postRouter.router)

#---user-routes
app.include_router(userRouter.router)


