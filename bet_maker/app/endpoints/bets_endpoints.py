import decimal
from typing import List

from fastapi import APIRouter, Depends

from business_model.bet import BetBusinessModel
from database import DbSession as async_session
from schemas.bet_schema import BetGet

router = APIRouter()


@router.get("/bets", tags=["Bet"], response_model=List[BetGet])
async def get_bets(bet_business_model: BetBusinessModel = Depends()):
    """
    Апи для получения всех сущностей ставок

    :param bet_business_model: Бизнес модель, в которой хранится логика ставки
    """
    async with async_session() as session:
        bet = await bet_business_model.get(session)
    return bet


@router.post("/{event_id}", tags=["Bet"], response_model=BetGet)
async def create_bet(event_id: int, bet_sum: decimal.Decimal, bet_business_model: BetBusinessModel = Depends()):
    """
    Апи для создания ставки

    :param event_id: идентификатор сущности события
    :param bet_sum: сумма ставки
    :param bet_business_model: Бизнес модель, в которой хранится логика ставки
    """
    async with async_session() as session:
        return await bet_business_model.create(session, event_id, bet_sum)
