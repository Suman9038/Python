from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter
from .. import models,schemas,utils
from ..database import engine,get_db
from sqlalchemy.orm import Session

router=APIRouter(tags=["User"])


@router.post("/users",status_code=status.HTTP_201_CREATED,response_model=schemas.UserResponse)
def CreateUser(user :schemas.CreateUser ,db: Session=Depends(get_db)) :
    # Hash the Passworda - Which can be retrive from user.password

    hashed_password=utils.hash(user.password)
    user.password=hashed_password

    new_user = models.User(**user.dict()) #title= new_post.title ye sab nahi karka siko asia newpost ko key value pair m karka kar skta h
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/users",response_model=list[schemas.UserResponse]) 
def getUser(db : Session = Depends(get_db)) :
    allUser=db.query(models.User).all()
    return allUser

@router.get("/users/{id}",response_model=list[schemas.UserResponse])
def getUserId(id : int ,db : Session = Depends(get_db)) :
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with this {id} does not exit")
    return [user]