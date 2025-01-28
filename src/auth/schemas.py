from pydantic import BaseModel, Field


class TokenData(BaseModel):
    email: str = Field(alias="sub")
    is_admin: bool = False


class AccessTokenResponse(BaseModel):
    access_token: str

