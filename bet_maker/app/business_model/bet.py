import decimal
from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from logger import logger
from models.bet_models import Bet
from schemas.bet_schema import BetCreate


class BetBusinessModel:

    @staticmethod
    async def create(session: AsyncSession, event_id: int, bet_sum: decimal.Decimal) -> BetCreate:
        """
        Создаем сущность ставки

        :param session: сессия для бд
        :param event_id: идентификатор события
        :param bet_sum: сумма ставки
        :return: BetCreate
        """
        bet = Bet(event_id=event_id, bet_sum=bet_sum)
        session.add(bet)
        await session.commit()
        logger.info(f"Была создана ставка {bet.id} на событие {event_id}")
        return bet

    @staticmethod
    async def get(session: AsyncSession) -> Sequence[Bet]:
        """
        Получаем все сущности ставки

        :param session: асинхронная сессия
        :return:
        """

        results = await session.execute(select(Bet))
        return results.scalars().all()
