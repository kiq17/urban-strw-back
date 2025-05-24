from fastapi import APIRouter, Depends, HTTPException, Request
from ..schemas.userSchema import User, UserRes
from ..schemas.loginSchema import Login, LoginRes
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models, utils, auth
from typing import List
from datetime import datetime, timezone, timedelta
import smtplib
from ..config import settings
from ..email import makeEmailTemplate
from uuid import uuid4
from random import randint
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/users", tags=["users"])



@router.post("/login")
def userLogin(user: Login, db: Session = Depends(get_db)):
    findUser = db.query(models.User).filter(models.User.email == user.email).first()

    if findUser is None:
        raise HTTPException(status_code=401, detail="Email ou senha inválidos")

    checkPass = utils.verify(user.senha, findUser.senha)

    if not checkPass:
        raise HTTPException(status_code=401, detail="Email ou senha inválidos")

    access_token = auth.createToken(data={"user_id": findUser.id})

    response = JSONResponse(content={"user": findUser.nome, "hash": utils.hash(findUser.nome)})

    ## 7 days cookie
    response.set_cookie(key="access_token", value=f"Bearer {access_token}", httponly=True)
    return response


# passar como parametro o schema para validar 
@router.get("/", response_model=List[UserRes])
def getUser(db: Session = Depends(get_db)):

    users = db.query(models.User).all()
    return users


@router.post("/", status_code=201, response_model=UserRes)
def createUser(user: User, db: Session = Depends(get_db)):

    findUser = db.query(models.User).filter(models.User.email == user.email).first()

    if findUser: 
        raise HTTPException(status_code=400, detail="Email já cadastrado")

    # hash senha função do arquivo utils
    hashedPass = utils.hash(user.senha)
    user.senha =  hashedPass
    

    # em vez de passar nome=user.nome etc
    # ** é como desustrurar um objeto js user dict tranforma em objeto
    userDict = user.dict()
    userDict.pop("preferences") 
    u = models.User(**userDict)
   
    db.add(u)
    db.commit()
    db.refresh(u)
    
    objects = list(map(lambda item: models.Preferences(choice=item, user_id=u.id), user.preferences))
    db.bulk_save_objects(objects)
    db.commit()

    return u

@router.put("/{id}", response_model=UserRes)
def editUser(id: int, user: User, db: Session = Depends(get_db)):
    userQuery = db.query(models.User).filter(models.User.id == id)

    findUser = userQuery.first()

    if findUser is None:
        raise HTTPException(status_code=404, detail="Usário não existe")
    
    hashedPass = utils.hash(user.senha)
    newUser = user.dict()
    newUser["update_at"] = datetime.now()
    newUser["senha"] = hashedPass

    userQuery.update(newUser, synchronize_session=False)

    db.commit()

    return userQuery.first()

@router.get("/{id}", response_model=UserRes)
def getUserId(id: int, db: Session = Depends(get_db)):
    findUser = db.query(models.User).filter(models.User.id == id).first()
    
    if findUser is None:
        raise HTTPException(status_code=404, detail="Usário não existe")
    
    return findUser

@router.post("/otp/{userId}", status_code=201)
def createOtp(userId: int, db: Session = Depends(get_db)):
    findUser = db.query(models.User).filter(models.User.id == userId).first()


    if findUser is None:
        raise HTTPException(status_code=404, detail="Usário não existe")
    

    EMAIL_SMTP = settings.email_smtp
    EMAIL_USER = settings.email_user
    EMAIL_PASS = settings.email_pass
    EMAIL_PORT = settings.email_port
    
    otp = models.Otps(temp_link=uuid4(), user_id=findUser.id, code=randint(100000, 999999))

    db.add(otp)
    db.commit()

    email_template = makeEmailTemplate(findUser.email, findUser.nome, otp.code)

    with smtplib.SMTP_SSL(EMAIL_SMTP, EMAIL_PORT) as smtp:
        smtp.login(EMAIL_USER, EMAIL_PASS)
        smtp.sendmail(EMAIL_SMTP, findUser.email, email_template)

    return {"tempLink": otp.temp_link}
    
@router.get("/check/{tempLink}")
def check_otp(tempLink: str, db: Session = Depends(get_db)):
    findOtp = db.query(models.Otps).filter(models.Otps.temp_link == tempLink).first()


    if findOtp is None:
        raise HTTPException(status_code=404, detail="Código inválido")
    
    # print(findUser.created_at)
    # data saved in db use different timezone
    db_timezone = timezone(timedelta(hours=0))
    now_date = datetime.now()
    now_date = now_date.astimezone(db_timezone)

    check_minutes = utils.is_valid_otp(now_date, findOtp.created_at)

    if check_minutes == True:
        db.query(models.Otps).filter(models.Otps.temp_link == tempLink).delete()
        db.commit()
        raise HTTPException(status_code=400, detail="Códgido expirado")
       
       
    return {"detail": "Código válido"}
       
    