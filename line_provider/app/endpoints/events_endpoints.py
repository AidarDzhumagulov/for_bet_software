from fastapi import APIRouter, Depends

from crud.event import EventBusinessModel
from database import DbSession as async_session
from schemas.event_schema import EventGet

router = APIRouter()


@router.get("/events", tags=['Event'], response_model=EventGet)
async def get_events(event: EventBusinessModel = Depends()):
    async with async_session() as session:
        events = await event.get_events(session)
    return events
