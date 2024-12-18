from jose import JWTError,jwt
from datetime import datetime,timedelta
from .import schemas
from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme=OAuth2PasswordBearer(tokenUrl="login")
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data : dict) :
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES) # To calculate time for expiration of the token
    to_encode.update({"exp" : expire})

    encoded_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)

    return encoded_jwt


def verify_access_token(token : str,credential_expectation) : 
    try : 
        decoded_jwt =jwt.decode(token,SECRET_KEY,algorithms=ALGORITHM)
        id = decoded_jwt.get("user_id")
        if not id : 
            raise credential_expectation
        token_data = schemas.TokenData(id=id)
    except JWTError :
        raise credential_expectation
    
    return token_data



def get_current_user(token : str = Depends(oauth2_scheme)) :
    credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=f"Could Not Validate Credential",headers={"WWW-Authenticate" : "Bearer"})
    return verify_access_token(token,credential_exception)