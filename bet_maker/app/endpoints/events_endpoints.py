import decimal
from datetime import datetime

from fastapi import APIRouter, Depends

from business_model.event import EventBusinessModel

router = APIRouter()


@router.get("/events", tags=['Event'])
async def get_events(event: EventBusinessModel = Depends()):
    return await event.get_events()


@router.post("/events", tags=['Event'])
async def get_events(coefficient: decimal.Decimal, deadline: datetime, event: EventBusinessModel = Depends()):
    return await event.create_events(coefficient, deadline)
