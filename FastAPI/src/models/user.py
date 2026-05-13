from pydantic import BaseModel, EmailStr, Field;
from datetime import datetime;

class User(BaseModel):
    name: str = Field(..., description="Full Name is Required");
    email: EmailStr = Field(..., description="Email is Required");
    password: str = Field(..., description="Password is Required");
    created_at: datetime = Field(default_factory=datetime.now);

class LoginUser(BaseModel):
    email: EmailStr = Field(..., description="Email is Required");
    password: str = Field(..., description="Password is Required");

class UpdateUser(BaseModel):
    name: str = Field(None, description="Name is optional");
    updated_at: datetime = Field(default_factory=datetime.now);