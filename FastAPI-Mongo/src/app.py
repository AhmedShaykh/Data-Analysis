from fastapi.exceptions import RequestValidationError;
from fastapi.middleware.cors import CORSMiddleware;
from src.routes.auth import router as AuthRoute;
from src.routes.task import router as TaskRoute;
from fastapi.responses import JSONResponse;
from fastapi import FastAPI;

app = FastAPI(
    title="Full Stack Fast API",
    description="Full Stack Fast Authentication Rest APIs With MongoDB",
    version="1.0.0"
);

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
);

app.include_router(AuthRoute);

app.include_router(TaskRoute);

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    errors = {}

    for error in exc.errors():

        field = error["loc"][-1];

        errors[field] = error["msg"];

    return JSONResponse(
        status_code=422,
        content={
            "message": "Validation Error",
            "errors": errors
        }
    );