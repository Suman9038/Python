from fastapi import FastAPI,Response,status,HTTPException,Depends
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
import mysql.connector
from mysql.connector import errorcode
import time
from sqlalchemy.orm import Session
from . import models,schemas,utils
from .database import engine,get_db
from .routers import post,user,auth


models.Base.metadata.create_all(bind=engine)

app=FastAPI()


while True :
    try :
        conn= mysql.connector.connect(user="root",password="suman2003",host="localhost",database="fastapi")
        cursor=conn.cursor(dictionary=True)
        print("DATABASE CONNECTION WAS SUCCESSFULL!!")
        break

    except mysql.connector.Error as err :
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else :
            print(err)
        time.sleep(3)
    else :
        conn.close()



# my_posts=[{"title":"HI Guys I am Suman","content":"I am Pursuing Btech","id":1},
#           {"title":"HI Guys I am Ankit","content":"I am Pursuing BCA","id":2}]

# def find_post(id) :
#     for i in my_posts :
#         if i['id'] == id :
#             return i
        
# def find_index_post(id : int) : 
#     for index , post in enumerate(my_posts) :
#         if post["id"] == id :
#             return index
#     return None


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
def root () :
    return{"Message":"Hello world"}

# @app.get("/sqlalchemy") 
# def test_req(db : Session = Depends(get_db)) :
#     posts=db.query(models.Post).all()
#     return{"data" : posts}






# @app.get("/posts/recent/latest")
# def get_latest() :
#     post=my_posts[len(my_posts)-1]
#     return{"data" : f"The Latest post is {post}"}



# For The User 


