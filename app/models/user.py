from pydantic import BaseModel, Field, EmailStr
import re
from typing import Annotated,Optional
from datetime import datetime

USERNAME_REGEX = re.compile(r"^[a-zA-Z0-9_.-]+$")

class UserCreate(BaseModel):
    username: str = Field(
        ...,
        min_length=3,
        max_length=50,
        pattern=USERNAME_REGEX.pattern,
        description="Kullanıcı adı; yalnızca harf, rakam, alt çizgi, nokta ve tire içerebilir"
    )

    first_name: str = Field(
        ...,
        min_length=2,
        max_length=50,
        description="Kullanıcının Adı"
    )

    last_name: str = Field(
        ...,
        min_length=2,
        max_length=50,
        description="Kullanıcının Soyadı"
    )
    email: EmailStr = Field(
        ...,
        description="Geçerli bir e-posta adresi"
    )
    password: str = Field(
        ...,
        min_length=8,
        description="Şifre; en az 8 karakter uzunluğunda olmalıdır"
    )
class UserLogin(BaseModel):
    username: Annotated[str, Field(...,min_length=3,max_length=30)]
    password: Annotated[str, Field(...,min_length=8)]

class UserRead(BaseModel):
    id: int
    username: str
    first_name: str
    last_name: str
    email: EmailStr
    is_active: bool
    created_at: datetime
    updated_at: datetime
    last_login: Optional[datetime] = None
    avatar_url: Optional[str] = None

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

UserCreate.model_rebuild()
Token.model_rebuild()
