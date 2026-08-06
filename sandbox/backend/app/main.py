from contextlib import asynccontextmanager

from fastapi import FastAPI

from backend.app.api import modules_router
from backend.app.bootstrap import bootstrap


@asynccontextmanager
async def lifespan(app: FastAPI):
    bootstrap()
    yield


app = FastAPI(
    title="Simple Solutions Practice",
    lifespan=lifespan,
)

app.include_router(modules_router)


@app.get("/")
def root():
    return {
        "status": "ok",
        "application": "Simple Solutions Practice",
    }