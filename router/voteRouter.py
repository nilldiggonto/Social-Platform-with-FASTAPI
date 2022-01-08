from fastapi import FastAPI,status,HTTPException,Depends,APIRouter
from starlette.routing import Router
from sqlalchemy.orm import Session
from db.models import Rate
from schema.schema import RateSchema
from db.db_connect import get_db
from utils.oauth2 import get_user

router = APIRouter(
    prefix= "/rate",
    tags= ["Rating"],
)

@router.post('/',status_code=status.HTTP_201_CREATED)
def rateView(request:RateSchema,db:Session = Depends(get_db), current_user:int = Depends(get_user)):
    rate_query = db.query(Rate).filter(Rate.post_id==request.post_id,Rate.user_id==current_user.id)
    check_rate = rate_query.first()
    
    if request.rate:
        if check_rate:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="User Already Rated")
        new_rate = Rate(post_id=request.post_id,user_id=current_user.id)
        db.add(new_rate)
        db.commit()
        return {'status':'success','message':'Rate Added'}
    else:
        if not check_rate:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No query Found")
        rate_query.delete(synchronize_session=False)
        db.commit()
        return {'status':'success','message':'Rate Removed'}
    
        






        
