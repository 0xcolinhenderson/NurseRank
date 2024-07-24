
from pydantic import BaseModel, EmailStr, Field, field_validator

class AccountValidator(BaseModel):
    firstname: str = Field(..., min_length=1, max_length=15)
    lastname: str = Field(..., min_length=1, max_length=15)
    email: EmailStr = ...
    password: str = ...

    @field_validator('firstname')
    def firstname_valid(cls, v):
        if not v[0].isalpha():
            raise ValueError('Firstname must start with a letter')
        if not v.isalnum():
            raise ValueError('Firstname must contain only letters, numbers, and underscores')
        return v
    
    @field_validator('lastname')
    def lastnamename_valid(cls, v):
        if not v[0].isalpha():
            raise ValueError('Firstname must start with a letter')
        if not v.isalnum():
            raise ValueError('Firstname must contain only letters, numbers, and underscores')
        return v

class EmailValidator(BaseModel):
    email: EmailStr