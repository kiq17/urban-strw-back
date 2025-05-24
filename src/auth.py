from jose import JWTError, jwt
from datetime import datetime, timedelta
from .schemas import loginSchema
from fastapi import HTTPException, Depends
from .config import settings
from .utils import OAuth2PasswordBearerWithCookie

authMid = OAuth2PasswordBearerWithCookie(tokenUrl="users/login")

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACESS_TOKEN_EXPIRE_MINUTES = settings.acess_token_expire_minutes # sven days

# create token
def createToken(data: dict):
    encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACESS_TOKEN_EXPIRE_MINUTES)
    encode.update({"exp": expire})

    token = jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

    return token

# checando token

def verifyToken(token: str, credentialExcept):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        
        id: str = payload.get("user_id")

        if id is None:
            raise credentialExcept
        token_data = loginSchema.TokenData(id=id)
    except JWTError:
        raise credentialExcept
    
    return token_data

def getCurrentUser(token: str = Depends(authMid)):
    credentialExcept = HTTPException(status_code=401, detail="Acesso Negado.")

    return verifyToken(token, credentialExcept)