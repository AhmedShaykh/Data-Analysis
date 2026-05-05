from todoModel import TodoModel,todoHelper;
from database import TodoCollection;
from fastapi import FastAPI;
from bson import ObjectId;

app = FastAPI();

TodoCollection = TodoCollection["fastAPI"];

@app.get("/", tags=["Todo"])
async def viewData():
    data =  await TodoCollection.find().to_list(length=None);
    all_todos=[];
    for todo in data:
        all_todos.append(todoHelper(todo));
    return all_todos;

@app.post("/", tags=["Todo"])
async def createView(data:TodoModel):
    result= await TodoCollection.insert_one(dict(data));
    print(result);
    return { "message" : data };

@app.put("/{id}", tags=["Todo"])
async def updateByid(id:str,data:TodoModel):
    data= await TodoCollection.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(data)
    });
    print(data);
    return { "message" : "Todo Updated" };

@app.delete("/{id}", tags=["Todo"])
async def deleteById(id:str):
    data= await TodoCollection.find_one_and_delete({"_id":ObjectId(id)});
    print(data);
    return { "message" : "Todo Deleted" };