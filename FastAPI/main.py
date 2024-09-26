from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app=FastAPI()

class Post(BaseModel) :
    title : str
    content : str
    published : bool = True 
    rating: Optional[int]=None

my_posts=[{"title":"HI Guys I am Suman","content":"I am Pursuing Btech","id":1},
          {"title":"HI Guys I am Ankit","content":"I am Pursuing BCA","id":2}]

def find_post(id) :
    for i in my_posts :
        if i['id'] == id :
            return i

@app.get("/")
def root () :
    return{"Message":"Hello world"}

@app.get("/posts")
def get_Post() :
    return{"Data":my_posts}

@app.post("/posts")
def createPost(new_post: Post) :
    #  print(new_post.published)
    #  print(new_post.rating)
    # print(new_post)
    # print(new_post.dict())
    next_post=new_post.dict() 
    next_post['id']=randrange(0,100000)
    my_posts.append(next_post)
    return {"data":next_post}

@app.get("/posts/{id}")
def get_Data(id:int ) :
    post =find_post(int(id))
    return{"data" : post}