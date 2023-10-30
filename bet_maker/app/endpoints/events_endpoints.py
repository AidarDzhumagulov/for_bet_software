import decimal
from datetime import datetime
from typing import List

from fastapi import APIRouter, Depends

from business_model.event import EventBusinessModel
from schemas.event_schema import EventGet

router = APIRouter()


@router.get("/events", tags=['Event'])
async def get_events(event: EventBusinessModel = Depends()) -> str:
    """
    Получение всех событий, с фильтрацией

    :param event: Бизнес модель События
    """
    return await event.get_events()


@router.post("/events", tags=['Event'])
async def create_events(coefficient: decimal.Decimal, deadline: datetime, event: EventBusinessModel = Depends()):
    """
    Апи для создания события

    :param coefficient: коэффициент события
    :param deadline: дата окончания события. Пример, 2023-11-05 23:59:00
    :param event: Бизнес модель События
    """
    return await event.create_events(coefficient, deadline)
