from contextlib import asynccontextmanager

from fastapi import FastAPI

from backend.app.bootstrap import bootstrap


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.platform = bootstrap()

    yield

    # Здесь позже появится:
    # app.state.platform.stop_all()


app = FastAPI(
    title="Simple Solutions Practice",
    lifespan=lifespan,
)


@app.get("/")
def root():
    return {
        "status": "ok",
        "application": "Simple Solutions Practice",
    }