from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class UserOutput(UserBase):
    id: int

    class Config:
        orm_mode = True


class UserUpdate(UserBase):
    ...
