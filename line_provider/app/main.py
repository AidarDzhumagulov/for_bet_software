import uvicorn
from fastapi import FastAPI
from endpoints.events_endpoints import router as event_router


def get_application() -> FastAPI:
    route = FastAPI()
    route.include_router(event_router, tags=["Event"], prefix="/event")
    return route


app = get_application()


@app.get("/")
def healthcheck():
    return {"message": "success"}


# For debugging
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
