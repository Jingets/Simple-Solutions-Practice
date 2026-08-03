from fastapi import FastAPI

app = FastAPI(title="Simple Solutions Practice")


@app.get("/")
def root():
    return {
        "status": "ok",
        "application": "Simple Solutions Practice",
    }
