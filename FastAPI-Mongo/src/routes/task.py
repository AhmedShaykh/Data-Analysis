from src.models.task import Task as TaskModel, UpdateTask, transformTask;
from fastapi import APIRouter, HTTPException, Depends;
from src.routes.auth import get_current_user;
from src.config.db import db as MongoDB
from bson import ObjectId;

taskCollection = MongoDB["task"];

router = APIRouter(prefix="/api/task", tags=["Task"]);

@router.get("", tags=["Task"], summary="Get All Tasks")
async def getAllTasks(user: str = Depends(get_current_user)):

    tasks = [];

    docs = await taskCollection.find({"user_id": user}).to_list(length=None);

    for task in docs:

        tasks.append(transformTask(task));

    return tasks;

@router.post("", tags=["Task"], summary="Create A New Task")
async def createTask(task: TaskModel, user: str = Depends(get_current_user)):

    data = task.dict();

    data["user_id"] = user;

    result = await taskCollection.insert_one(data);

    return {
        "message": "Task Created!",
        "id": str(result.inserted_id)
    };

@router.get("/{id}", tags=["Task"], summary="Get Task By ID")
async def getTask(id: str, user: str = Depends(get_current_user)):

    try:

        task = await taskCollection.find_one({"_id": ObjectId(id), "user_id": user});

        if not task:

            raise HTTPException(
                status_code=404,
                detail="Task Not Found"
            );

        return transformTask(task);

    except:

        raise HTTPException(
            status_code=400,
            detail="Invalid Task ID"
        );

@router.put("/{id}", tags=["Task"], summary="Update Task")
async def updateTask(id: str, task: UpdateTask, user: str = Depends(get_current_user)):

    try:

        updatedTask = await taskCollection.update_one(
            {"_id": ObjectId(id), "user_id": user},
            {"$set": task.dict(exclude_none=True)}
        );

        if updatedTask.modified_count == 0:
            
            raise HTTPException(
                status_code=404,
                detail="Task Not Found Or No Changes Made"
            );

        return { "message": "Task Updated!" };

    except:
        
        raise HTTPException(
            status_code=400,
            detail="Invalid Task ID"
        );

@router.delete("/{id}", tags=["Task"], summary="Delete Task")
async def deleteTask(id: str, user: str = Depends(get_current_user)):

    try:

        deletedTask = await taskCollection.delete_one({"_id": ObjectId(id), "user_id": user});

        if deletedTask.deleted_count == 0:

            raise HTTPException(
                status_code=404,
                detail="Task Not Found"
            );

        return { "message": "Task Deleted!" };

    except:
        
        raise HTTPException(
            status_code=400,
            detail="Invalid Task ID"
        );