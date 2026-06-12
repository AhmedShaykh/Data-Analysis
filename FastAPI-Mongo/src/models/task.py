from pydantic import BaseModel, Field;
from datetime import datetime;
from typing import Optional;

class Task(BaseModel):
    title: str = Field(...);
    desc: str = Field(...);
    is_complete: Optional[bool] = False;
    created_at: datetime = Field(default_factory=datetime.now);

class UpdateTask(BaseModel):
    title: Optional[str] = None;
    desc: Optional[str] = None;
    is_complete: Optional[bool] = None;
    updated_at: datetime = Field(default_factory=datetime.now);

def transformTask(task):
    task["_id"] = str(task["_id"]);
    return task;