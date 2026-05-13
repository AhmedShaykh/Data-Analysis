from config.db import db as MongoDB;
from datetime import datetime;

blacklistCollection = MongoDB["blacklist_tokens"];

async def create_indexes():
    await blacklistCollection.create_index("token", unique=True);
    await blacklistCollection.create_index("createdAt", expireAfterSeconds=86400);

async def blacklist_token(token: str):
    await blacklistCollection.insert_one({
        "token": token,
        "createdAt": datetime.now()
    });

async def is_blacklisted(token: str) -> bool:
    doc = await blacklistCollection.find_one({"token": token});
    return doc is not None;