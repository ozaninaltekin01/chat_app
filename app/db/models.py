from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    #Kullanıcı hesabı için gerekli alanlar
    username: str = Field(index=True,unique=True,min_length=3,max_length=50)
    first_name: str = Field(min_length=2,max_length=50)
    last_name: str = Field(min_length=2,max_length=50)
    email: str = Field(index=True,unique=True,min_length=5,max_length=100)
    hashed_password: str

    #opisyonel/ek bilgiler
    is_acitve: bool = Field(default=True)
    crated_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    last_login: Optional[datetime] = None
    avatar_url: Optional[str] = None