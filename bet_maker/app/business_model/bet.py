import decimal

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models.bet_models import Bet
from schemas.bet_schema import BetGet, BetCreate
from logger import logger


class BetBusinessModel:

    @staticmethod
    async def create(session: AsyncSession, event_id: int, bet_sum: decimal.Decimal) -> BetCreate:
        """
        Создаем сущность ставки

        :param session:
        :param event_id:
        :param bet_sum:
        :return:
        """
        bet = Bet(event_id=event_id, bet_sum=bet_sum)
        session.add(bet)
        await session.commit()
        logger.info(f"Была создана ставка {bet.id} на событие {event_id}")
        return bet

    @staticmethod
    async def get(session: AsyncSession):
        """
        Получаем все сущности ставки

        :param session: асинхронная сессия
        :return:
        """

        results = await session.execute(select(Bet))
        return results.scalars().all()
