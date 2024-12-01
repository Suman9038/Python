from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Optional,Union
class PostBase(BaseModel) :
    title : str
    content : str
    published : bool = True 

# class Create_Post(BaseModel) :
#     title : str
#     content : str
#     published : bool = True 

            #OR

class Create_Post(PostBase) : # simply inherit karo PostBase ka toh waara sara chiz aa hi jayega or baki pass krdo q ki or kuch karna h nahi filala
    pass


# class Update_Post(BaseModel) :
#     title : str
#     content : str
#     published : bool 

                #OR
class Update_Post(PostBase) :
    pass


class PostResponse(PostBase) :
    id : int
    created_at : datetime

    class config :
        orm_mode=True

class CreateUser(BaseModel) :
    email :EmailStr
    password :str

class UserResponse(BaseModel) :
    id : int
    email : str
    created_at : datetime

    class config :
        orm_mode=True


class UserLogin(BaseModel) :
    email : EmailStr
    password : str

class Token(BaseModel) :
    access_token : str
    token_type : str

class TokenData(BaseModel) :
    id : Union[int,None]