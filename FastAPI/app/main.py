from fastapi import FastAPI,Response,status,HTTPException,Depends
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
import mysql.connector
from mysql.connector import errorcode
import time
from sqlalchemy.orm import Session
from . import models
from .database import engine,get_db

models.Base.metadata.create_all(bind=engine)

app=FastAPI()

class Post(BaseModel) :
    title : str
    content : str
    published : bool = True 

while True :
    try :
        conn= mysql.connector.connect(user="root",password="Suman2003",host="localhost",database="fastapi")
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



my_posts=[{"title":"HI Guys I am Suman","content":"I am Pursuing Btech","id":1},
          {"title":"HI Guys I am Ankit","content":"I am Pursuing BCA","id":2}]

def find_post(id) :
    for i in my_posts :
        if i['id'] == id :
            return i
        
def find_index_post(id : int) : 
    for index , post in enumerate(my_posts) :
        if post["id"] == id :
            return index
    return None

@app.get("/")
def root () :
    return{"Message":"Hello world"}

@app.get("/sqlalchemy") 
def test_req(db : Session = Depends(get_db)) :
    return{"data" : "successful"}


@app.get("/posts")
def get_Post() :
    cursor.execute("SELECT * FROM posts")
    posts=cursor.fetchall()
    print(posts)
    return{"Data":posts}

@app.post("/posts",status_code=status.HTTP_201_CREATED)
def createPost(new_post: Post) :
    #  print(new_post.published)
    #  print(new_post.rating)
    # print(new_post)
    # print(new_post.dict())
    # next_post=new_post.dict() 
    # next_post['id']=randrange(0,100000)
    # my_posts.append(next_post)

    # cursor.execute(f"INSERT INTO posts(title,content,published) VALUES({new_post.title,new_post.content,new_post.published})")

    # KOI V LIKH SKTA H JO MAAN HO UPAR WALA YA NICHE WALA 

    cursor.execute("INSERT INTO posts(title,content,published) VALUES (%s, %s, %s) ",(new_post.title,new_post.content,new_post.published))
    next_post=cursor.fetchone()
    conn.commit()
    return {"data":next_post}

@app.get("/posts/{id}")
def get_Data(id : int , response : Response) :
    cursor.execute("SELECT * FROM posts WHERE id = %s", (id,))
    post=cursor.fetchone()
    print(post)
    # post =find_post(int(id))
    if not post :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail= f"The id = {id} data not found")
        # response.status_code= status.HTTP_404_NOT_FOUND 
        # return{"message" : f"The id = {id} data not found"}
    return{"data" : post}

@app.get("/posts/recent/latest")
def get_latest() :
    post=my_posts[len(my_posts)-1]
    return{"data" : f"The Latest post is {post}"}

@app.delete("/posts/delete/{id}",status_code= status.HTTP_204_NO_CONTENT)
def delete_post(id : int) :
    cursor.execute("DELETE FROM posts WHERE id =%s",(id,))
    deleted_post=cursor.fetchone()
    conn.commit()
    # index = find_index_post(id)
    if delete_post is None :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"The id you have given that is {id} that does not exist")
    # my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/update/{id}")
def update_posts(id : int , post: Post) :
    # print(post) 
    cursor.execute("UPDATE posts SET title = %s , content = %s , published = %s WHERE id = %s",(post.title,post.content,post.published,id))
    updated_posts=cursor.fetchone()
    conn.commit()
    # index = find_index_post(id)
    if updated_posts == None :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"The id you have given that is {id} that does not exist")
    # post_dict=post.dict()
    # post_dict["id"]=id
    # my_posts[index]=post_dict
    return{"data" : updated_posts}


