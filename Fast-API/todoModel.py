from pydantic import BaseModel;
from datetime import datetime;
from typing import Union;

class TodoModel(BaseModel):
    title : str; 
    desc : str; 
    isComplete : Union[bool,None] = False;
    created_at : Union[datetime,None] = datetime.utcnow();

def todoHelper(todo) -> dict:
    return {
        "id": str(todo["_id"]),
        "title": todo["title"],
        "desc": todo["desc"],
        "isComplete": todo["isComplete"],
        "created_at": todo["created_at"]
    };