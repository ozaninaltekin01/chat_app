from fastapi import APIRouter, HTTPException,Depends,status
from sqlmodel import select
from app.db.session import get_session
from app.db.models import User
from app.models.user import  UserCreate,Token,UserLogin
from app.core.security import get_password_hash,create_access_token,verify_password
from sqlalchemy import or_

router=APIRouter()

@router.get("/ping")
async def ping():
    return {"pong": "ok"}

@router.post(
    "/register",
    response_model=Token,
    status_code=status.HTTP_201_CREATED,)
def register(
        user_in: UserCreate,
        session=Depends(get_session)
):

    existing= session.exec(
        select(User).where(
            or_(
                User.username == user_in.username,
                User.email == user_in.email
            )
        )

    ).first()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Kullanıcı adı veya e-posta zaten mevcut"
        )

    hashed=get_password_hash(user_in.password)
    user=User(
        username=user_in.username,
        first_name=user_in.first_name,
        last_name=user_in.last_name,
        email=user_in.email,
        hashed_password=hashed
    )

    session.add(user)
    session.commit()
    session.refresh(user)

    token=create_access_token({"sub": user.username})
    return Token(access_token=token)

@router.post("/login", response_model=Token)
def login(
        user_in: UserLogin,
        session = Depends(get_session)
):
    user = session.exec(
        select(User).where(User.username == user_in.username)
    ).first()

    if not user or not verify_password(user_in.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Kullanıcı adı veya şifre hatalı",
        )

    token = create_access_token({"sub": user.username})
    return Token(access_token=token)
