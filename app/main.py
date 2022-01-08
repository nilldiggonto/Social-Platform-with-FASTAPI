from fastapi import FastAPI
from db.db_connect import Base,engine
from router import postRouter,userRouter,auth, voteRouter
from utils.oauth2 import SECRET_KEY
from config.config import settings

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

#----Authenticate
app.include_router(auth.router)

#---Rating
app.include_router(voteRouter.router)


