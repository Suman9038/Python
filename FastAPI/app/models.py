from .database import Base
from sqlalchemy import Column,Integer,String,Boolean

class Post(Base) :
    __tablename__="posts"

    id=Column(Integer,primary_key=True,nullable=False)
    title=Column(String(255),nullable=False)
    content=Column(String(255),nullable=False)
    published=Column(Boolean,default=True)