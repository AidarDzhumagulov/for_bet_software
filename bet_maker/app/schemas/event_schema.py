import datetime
import decimal

from pydantic import BaseModel
from typing import Optional

from models.event_models import EventState


class EventGet(BaseModel):
    id: int
    coefficient: Optional[decimal.Decimal]
    deadline: Optional[datetime.datetime]
    state: Optional[EventState]

    class Config:
        orm_mode = True
