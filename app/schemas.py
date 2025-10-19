

from pydantic import BaseModel, EmailStr, conint
from datetime import datetime
from typing import Optional

# Base class for shared fields
class PostBase(BaseModel):
    title: str
    content: str
    publish: bool = True


class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        orm_mode = True

# For creating a new post (inherits from PostBase)
class PostCreate(PostBase):

    pass

# For returning posts from the DB (can also include id or timestamps if needed)
class Post(PostBase):
    id: int
    create_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    create_at: datetime


    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int] = None

class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)















    
