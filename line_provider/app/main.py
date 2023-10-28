import uvicorn
from fastapi import FastAPI
# from endpoints.bets_endpoints import router as bet_router
from endpoints.events_endpoints import router as event_router
from database import Base, engine


def get_application() -> FastAPI:
    route = FastAPI()
    route.include_router(event_router, tags=["Event"], prefix="/event")
    # route.include_router(bet_router, tags=["Bet"], prefix="/bet")
    return route


app = get_application()


@app.on_event("startup")
async def startup_event():
    """Drop and create DB"""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


@app.get("/")
def healthcheck():
    return {"message": "success"}


# For debugging
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
