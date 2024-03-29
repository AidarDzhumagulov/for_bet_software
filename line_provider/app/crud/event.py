import decimal
from datetime import datetime

from sqlalchemy import Date
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.event_models import Event


class EventBusinessModel:

    def __init__(self):
        self.current_time = datetime.now().date()

    async def get_events(self, session: AsyncSession):
        """
        Получаем все события

        :param session:
        :return:
        """
        events = select(Event).filter(Event.deadline.cast(Date) > self.current_time)
        result = await session.execute(events)
        return result.scalars().all()

    @staticmethod
    async def create_event(session: AsyncSession, coefficient: decimal.Decimal, deadline: datetime):
        """
        Создаем событие

        :param session:
        :param coefficient:
        :param deadline:
        :return:
        """

        event = Event(coefficient=coefficient, deadline=deadline)
        session.add(event)
        await session.commit()
        return event
