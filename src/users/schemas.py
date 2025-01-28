from pydantic import BaseModel, ConfigDict, EmailStr, model_validator
from src.users.validators import Check_password, Check_phone


class UserBase(BaseModel):
    full_name: str
    email: EmailStr
    phone: Check_phone


class AuthUser(BaseModel):
    email: str
    password: str


class UserIn(UserBase):
    password: Check_password
    password_repeat: str


    @model_validator(mode="after")
    def check_password_match(self):
        if self.password != self.password_repeat:
            raise ValueError("Пароли не совпадают!")
        return self


class User(UserBase):
    model_config = ConfigDict(from_attributes=True)
    id: int