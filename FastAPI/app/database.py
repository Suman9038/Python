from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import mysql.connector
from mysql.connector import errorcode
import time
# from .config import settings

Database_URL="mysql://root:suman2003@localhost/fastapi"
# Database_URL=f"mysql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}/{settings.database_name}"

engine= create_engine(Database_URL)

Sessionlocal= sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base=declarative_base()

def get_db() :
    db=Sessionlocal() 
    try :
        yield db
    finally :
        db.close()


# while True :
#     try :
#         conn= mysql.connector.connect(user="root",password="suman2003",host="localhost",database="fastapi")
#         cursor=conn.cursor(dictionary=True)
#         print("DATABASE CONNECTION WAS SUCCESSFULL!!")
#         break

#     except mysql.connector.Error as err :
#         if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#             print("Something is wrong with your user name or password")
#         elif err.errno == errorcode.ER_BAD_DB_ERROR:
#             print("Database does not exist")
#         else :
#             print(err)
#         time.sleep(3)
#     else :
#         conn.close()
