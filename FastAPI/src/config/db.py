from dotenv import load_dotenv;
import motor.motor_asyncio;
import os;

load_dotenv();

url = os.getenv("DATABASE_URL");

if not url:
    raise ValueError("DATABASE_URL Not Found In Environment Variables!");

client = motor.motor_asyncio.AsyncIOMotorClient(url);

db = client["fastAPI"];

print("MongoDB Connected Successfully");