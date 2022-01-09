from fastapi import FastAPI
# from db.db_connect import Base,engine
from router import postRouter,userRouter,auth, voteRouter
# from fastapi.middleware.cors import CORSMiddleware 


app  = FastAPI()

# origins = [
#     "https://google.com"
# ]
# #----CORS
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )
#----------
#_____________
#
#CREATING DB
#______________
# Base.metadata.create_all(bind=engine) #Using alembic to generate tables 
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


