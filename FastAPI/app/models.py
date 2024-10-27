from .database import Base
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy import Column,Integer,String,Boolean

class Post(Base) :
    __tablename__="posts"

    id=Column(Integer,primary_key=True,nullable=False)
    title=Column(String(255),nullable=False)
    content=Column(String(255),nullable=False)
    published=Column(Boolean,server_default=text("True"))
    created_at=(Column(TIMESTAMP,nullable=False,server_default=text('now()')))