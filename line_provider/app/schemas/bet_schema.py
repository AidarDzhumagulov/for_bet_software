import decimal
from typing import Optional

from pydantic import BaseModel

from models.bet_models import BetState


class BetCreate(BaseModel):
    event_id: Optional[int]
    bet_sum: Optional[decimal.Decimal]


class BetGet(BaseModel):
    id: Optional[int]
    event_id: Optional[int]
    status: Optional[BetState]
    bet_sum: Optional[decimal.Decimal]

    class Config:
        orm_mode = True
