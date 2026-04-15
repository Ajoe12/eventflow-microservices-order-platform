from beanie import Document
from pydantic import EmailStr

class User(Document):
    email : EmailStr
    password : str
    role : str = "User"

    #sets collection name to users
    #else collection = lowercase class name => user
    class Settings:
        name = "users"