from pydantic import BaseModel, Field, EmailStr

class RegisterRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6)
    role: bool

class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6)
