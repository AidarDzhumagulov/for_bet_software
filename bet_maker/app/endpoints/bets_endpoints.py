import decimal

from fastapi import APIRouter, Depends

from business_model.bet import BetBusinessModel
from database import DbSession as async_session


router = APIRouter()


@router.get("/", tags=["Bet"])
async def get_bets(bet_business_model: BetBusinessModel = Depends()):
    async with async_session() as session:
        bet = await bet_business_model.get(session)
    return bet


@router.post("/{event_id}", tags=["Bet"])
async def create_bet(event_id: int, bet_sum: decimal.Decimal, bet_business_model: BetBusinessModel = Depends()):
    async with async_session() as session:
        return await bet_business_model.create(session, event_id, bet_sum)
