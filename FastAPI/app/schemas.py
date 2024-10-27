from pydantic import BaseModel

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
