from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter
from .. import models,schemas,utils,oauth2
from ..database import get_db
from sqlalchemy.orm import Session

router=APIRouter(tags=["Posts"])


@router.post("/posts",status_code=status.HTTP_201_CREATED,response_model=schemas.PostResponse)
def createPost(new_post: schemas.Create_Post,db : Session = Depends(get_db), user_id : int = Depends(oauth2.get_current_user)) :
    #  print(new_post.published)
    #  print(new_post.rating)
    # print(new_post)
    # print(new_post.dict())
    # next_post=new_post.dict() 
    # next_post['id']=randrange(0,100000)
    # my_posts.append(next_post)

    # cursor.execute(f"INSERT INTO posts(title,content,published) VALUES({new_post.title,new_post.content,new_post.published})")

    # KOI V LIKH SKTA H JO MAAN HO UPAR WALA YA NICHE WALA 

    # cursor.execute("INSERT INTO posts(title,content,published) VALUES (%s, %s, %s) ",(new_post.title,new_post.content,new_post.published))
    # next_post=cursor.fetchone()
    # conn.commit()
    next_post = models.Post(**new_post.dict()) #title= new_post.title ye sab nahi karka siko asia newpost ko key value pair m karka kar skta h
    db.add(next_post)
    db.commit()
    db.refresh(next_post)
    return next_post

@router.get("/posts",response_model=list[schemas.PostResponse])
def get_Post(db : Session = Depends(get_db), user_id : int = Depends(oauth2.get_current_user)) :
    # cursor.execute("SELECT * FROM posts")
    # posts=cursor.fetchall()
    # print(posts)
    posts=db.query(models.Post).all()
    return posts


@router.get("/posts/{id}",response_model=schemas.PostResponse)
def get_Data(id : int , response : Response,db : Session = Depends(get_db), user_id : int = Depends(oauth2.get_current_user)) :
    # cursor.execute("SELECT * FROM posts WHERE id = %s", (id,))
    # post=cursor.fetchone()
    # print(post)
    # post =find_post(int(id))
    post = db.query(models.Post).filter(models.Post.id==id).first()
    if not post :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail= f"The id = {id} data not found")
        # response.status_code= status.HTTP_404_NOT_FOUND 
        # return{"message" : f"The id = {id} data not found"}
    return post

@router.delete("/posts/delete/{id}",status_code= status.HTTP_204_NO_CONTENT)
def delete_post(id : int,db : Session = Depends(get_db), user_id : int = Depends(oauth2.get_current_user)) :
    # cursor.execute("DELETE FROM posts WHERE id =%s",(id,))
    # deleted_post=cursor.fetchone()
    # conn.commit()
    # index = find_index_post(id) if deleted_post.first() == None :
        # raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"The id you have given that is {id} that does not exist")
    # my_posts.pop(index)
    deleted_post = db.query(models.Post).filter(models.Post.id==id).delete(synchronize_session=False)
    db.commit()
    if deleted_post== 0 :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"The id you have given that is {id} that does not exist")
    # my_posts.pop(index)
    # deleted_post.delete(synchronize_session=False)
    # db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/posts/update/{id}",response_model=schemas.PostResponse)
def update_posts(id : int , post: schemas.Update_Post,db : Session = Depends(get_db), user_id : int = Depends(oauth2.get_current_user)) :
    # print(post) 
    # cursor.execute("UPDATE posts SET title = %s , content = %s , published = %s WHERE id = %s",(post.title,post.content,post.published,id))
    # updated_posts=cursor.fetchone()
    # conn.commit()
    # index = find_index_post(id)

    # 1 method to do 
    # updated_posts = db.query(models.Post).filter(models.Post.id==id)
    # if updated_posts.first() == None :
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"The id you have given that is {id} that does not exist")
    
    # updated_posts.update(post.dict(),synchronize_session=False)
    # db.commit()

    # 2 method 
    updated_posts = db.query(models.Post).filter(models.Post.id==id).update(post.dict(),synchronize_session=False)
    db.commit()
    if updated_posts == 0 :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"The id you have given that is {id} that does not exist")
    
    
    # post_dict=post.dict()
    # post_dict["id"]=id
    # my_posts[index]=post_dict
    return{"data" :"Post Updated Successfully "}