import decimal
from datetime import datetime

from fastapi import APIRouter, Depends

from crud.event import EventBusinessModel
from database import DbSession as async_session

router = APIRouter()


@router.get("/events", tags=['Event'])
async def get_events(event: EventBusinessModel = Depends()):
    async with async_session() as session:
        events = await event.get_events(session)
    return events


@router.post("/events", tags=["Event"])
async def create_event(coefficient: decimal.Decimal, deadline: datetime, event: EventBusinessModel = Depends()):
    async with async_session() as session:
        events = await event.create_event(session, coefficient, deadline)
    return events
