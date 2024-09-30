from fastapi import FastAPI,Response,status,HTTPException
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
        
def find_index_post(id : int) : 
    for index , post in enumerate(my_posts) :
        if post["id"] == id :
            return index
    return None

@app.get("/")
def root () :
    return{"Message":"Hello world"}

@app.get("/posts")
def get_Post() :
    return{"Data":my_posts}

@app.post("/posts",status_code=status.HTTP_201_CREATED)
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
def get_Data(id : int , response : Response) :
    post =find_post(int(id))
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
    index = find_index_post(id)
    if index is None :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"The id you have given that is {id} that does not exist")
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/update/{id}")
def updated_posts(id : int , post: Post) :
    # print(post) 
    index = find_index_post(id)
    if index is None :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"The id you have given that is {id} that does not exist")
    post_dict=post.dict()
    post_dict["id"]=id
    my_posts[index]=post_dict
    return{"data" : post_dict}


