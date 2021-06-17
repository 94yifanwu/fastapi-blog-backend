from pydantic import BaseModel
from typing import List, Optional


class BlogBase(BaseModel):
    tytle: str
    body: str


class Blog(BlogBase):
    class Config():
        orm_mode = True


class UserBase(BaseModel):
    name: str
    email: str
    password: str


class User(BlogBase):
    class Config():
        orm_mode = True


class ShowUserResponse(BaseModel):
    name: str
    email: str
    blogs: List[Blog] = []

    class Config():
        orm_mode = True


class ShowBlogResponse(BaseModel):
    title: str
    body: str
    creator: ShowUserResponse

    class Config():
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
