from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials;
from src.models.user import User as UserModel, LoginUser, UpdateUser;
from src.models.blacklist import blacklist_token, is_blacklisted;
from fastapi import APIRouter, HTTPException, status, Depends;
from datetime import datetime, timedelta;
from src.config.db import db as MongoDB;
from dotenv import load_dotenv;
import bcrypt;
import bson;
import jwt;
import os;

load_dotenv();

JWT_AUTH = os.getenv("JWT_SECRET");

security = HTTPBearer();

authCollection = MongoDB["auth"];

def create_token(user_id: str) -> str:

    payload = {
        "userId": user_id,
        "exp": datetime.utcnow() + timedelta(days=7),
        "iat": datetime.utcnow()
    };

    return jwt.encode(payload, JWT_AUTH, algorithm="HS256");

async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):

    try:

        token = credentials.credentials;

        if await is_blacklisted(token):

            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token Has Been Logged Out"
            );

        payload = jwt.decode(token, JWT_AUTH, algorithms=["HS256"]);

        return payload["userId"];

    except:
        
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or Expired Token"
        );

router = APIRouter(prefix="/api/auth", tags=["Auth"]);

@router.post("/register", summary="Register A New User")
async def registerUser(data: UserModel):

    data = data.dict();

    check_exist = await authCollection.find_one({"email": data["email"].lower()});

    if check_exist:
        
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User Already Exists With This Email"
        );

    salt = bcrypt.gensalt(10);

    data["password"] = bcrypt.hashpw(data["password"].encode(), salt).decode();

    data["email"] = data["email"].lower();

    doc = await authCollection.insert_one(data);

    document = await authCollection.find_one(
        {"_id": doc.inserted_id},
        {"name": 1, "email": 1}
    );

    document["_id"] = str(document["_id"]);

    token = create_token(document["_id"]);

    return {
        "msg": "User Registered Successfully",
        "token": token
    };

@router.post("/login", summary="Login User")
async def loginUser(data: LoginUser):

    data = data.dict();

    check_exist = await authCollection.find_one({"email": data["email"].lower()});

    if not check_exist:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No Account Found With This Email"
        );

    is_match = bcrypt.checkpw(data["password"].encode(), check_exist["password"].encode());

    if not is_match:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Credentials"
        );

    check_exist["_id"] = str(check_exist["_id"]);

    del check_exist["password"];

    token = create_token(check_exist["_id"]);

    return {
        "msg": "User Logged In Successfully",
        "token": token
    };

@router.post("/logout", summary="Log Out User")
async def logoutUser(credentials: HTTPAuthorizationCredentials = Depends(security)):

    token = credentials.credentials;

    if await is_blacklisted(token):

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="You Are Already Logged Out"
        );

    await blacklist_token(token);

    return {"msg": "User Logged Out Successfully"};

@router.get("/profile", summary="Get User Profile")
async def getProfile(user: str = Depends(get_current_user)):

    profile = await authCollection.find_one(
        {"_id": bson.ObjectId(user)},
        {"password": 0}
    );

    if not profile:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User Not Found"
        );

    profile["_id"] = str(profile["_id"]);

    return profile;

@router.put("/profile", summary="Update User Profile")
async def updateProfile(data: UpdateUser, user: str = Depends(get_current_user)):
    
    await authCollection.find_one_and_update(
        {"_id": bson.ObjectId(user)},
        {"$set": data.dict(exclude_none=True)}
    );

    return {"msg": "Profile Updated Successfully"};