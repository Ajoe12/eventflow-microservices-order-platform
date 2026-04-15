from pydantic import BaseModel, EmailStr

#define api request and response structure
#models is for directly mapping ti db collections
#model db layer
#schema api layer
class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str