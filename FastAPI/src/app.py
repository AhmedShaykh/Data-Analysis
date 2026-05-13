from fastapi.middleware.cors import CORSMiddleware;
from routes.auth import router as AuthRoute;
from routes.task import router as TaskRoute;
from fastapi import FastAPI;
import uvicorn;

app = FastAPI(
    title="Full Stack Task Manager API",
    description="Full Stack Authentication Task Manager Rest APIs",
    version="1.0.0"
);

origins = ["*"];

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
);

app.include_router(TaskRoute);

app.include_router(AuthRoute);

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True);