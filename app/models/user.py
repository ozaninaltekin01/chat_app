from pydantic import BaseModel, Field, EmailStr
import re

USERNAME_REGEX = re.compile(r"^[a-zA-Z0-9_.-]+$")

class UserCreate(BaseModel):
    username: str = Field(
        ...,
        min_length=3,
        max_length=50,
        regex=USERNAME_REGEX,
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


class Token(BaseModel):
    access_token: str
    token_type: "bearer"
