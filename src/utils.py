from passlib.context import CryptContext
from datetime import datetime
from fastapi.security import OAuth2
from fastapi.openapi.models import OAuthFlows as OAuthFlowsModel
from fastapi import Request
from fastapi.security.utils import get_authorization_scheme_param
from fastapi import HTTPException
from fastapi import status
from typing import Optional
from typing import Dict

pwdContext = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(password: str):
    return pwdContext.hash(password)

def verify(password: str, hashedPass: str):
    return pwdContext.verify(password, hashedPass)

def is_valid_otp(data_inicial: datetime, data_final: datetime) -> bool:

    # 2023-07-20 23:19:51.632066+00:00
    data_final = data_final.__str__()[:-13]

    # 2023-12-27 20:19:40.002128
    data_inicial = data_inicial.__str__()[:-13]

    then = datetime.strptime(data_final, '%Y-%m-%d %H:%M:%S')      
    now  = datetime.strptime(data_inicial, '%Y-%m-%d %H:%M:%S') 

    duration = now - then                         
    duration_in_s = duration.total_seconds()   

    minutes = divmod(duration_in_s, 60)[0] 

    return minutes >= 5 


class OAuth2PasswordBearerWithCookie(OAuth2):
    def __init__(
        self,
        tokenUrl: str,
        scheme_name: Optional[str] = None,
        scopes: Optional[Dict[str, str]] = None,
        auto_error: bool = True,
    ):
        if not scopes:
            scopes = {}
        flows = OAuthFlowsModel(password={"tokenUrl": tokenUrl, "scopes": scopes})
        super().__init__(flows=flows, scheme_name=scheme_name, auto_error=auto_error)

    async def __call__(self, request: Request) -> Optional[str]:
        authorization: str = request.cookies.get("access_token")  #changed to accept access token from httpOnly Cookie
        scheme, param = get_authorization_scheme_param(authorization)
        if not authorization or scheme.lower() != "bearer":
            if self.auto_error:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Not authenticated",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            else:
                return None
        return param