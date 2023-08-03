from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime

class fullDet(BaseModel):
    pid: int
    part_name: str
    mat_comp: str
    age: int
    condi: bool
    manufacturer: str
    aircraft_mod: str

    class Config:
        orm_mode=True

class superVis(BaseModel):
    recycleMat: dict
    repurposeMat: dict

    class Config:
        orm_mode=True

class signUpFacility(BaseModel):
    user_id: str
    pwd: str

    class Config:
        orm_mode=True

class signUp(signUpFacility):
    company: Optional[str]

    class Config:
        orm_mode=True


class RSignUp(BaseModel):
    user_id: str
    role: str 
    company: Optional[str]=None
    
    class Config:
        orm_mode=True
    
class signIn(BaseModel):
    user_id: str
    pwd: str

    class Config:
        orm_mode=True

class tokenData(BaseModel):
    user_id: str
    opt: str
    class Config:
        orm_mode = True

# class signUpInfo(BaseModel):
#     email: EmailStr
#     pwd: str

#     class Config:
#         orm_mode=True

# class resSignUpInfo(BaseModel):
#     user_id: int
#     role: str 
#     created_at: datetime
    
#     class Config:
#         orm_mode=True


# class loginCred(BaseModel):
#     email: EmailStr
#     pwd: str
        
#     class Config:
#         orm_mode=True

# class resToken(BaseModel):
#     user_id: int
#     token: str
        
#     class Config:
#         orm_mode=True

# class userPost(BaseModel):
#     id:Optional[int]
#     context: str
#     post: str
        
#     class Config:
#         orm_mode=True

# class resUserPost(BaseModel):
#     id: int
#     pid: int
#     context: str
#     post: str
#     created_at: datetime

#     class Config:
#         orm_mode=True

# class tokenData(BaseModel):
#     user_id: str
#     class Config:
#         orm_mode = True

