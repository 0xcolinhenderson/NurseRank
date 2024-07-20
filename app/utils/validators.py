
from pydantic import BaseModel, EmailStr, Field, field_validator

class AccountValidator(BaseModel):
    username: str = Field(..., min_length=1, max_length=15)
    email: EmailStr = ...
    password: str = ...

    @field_validator('username')
    def username_valid(cls, v):
        if not v[0].isalpha():
            raise ValueError('Username must start with a letter')
        if not v.isalnum():
            raise ValueError('Username must contain only letters, numbers, and underscores')
        return v

class EmailValidator(BaseModel):
    email: EmailStr