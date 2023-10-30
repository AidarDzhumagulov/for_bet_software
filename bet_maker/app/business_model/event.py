import decimal

import httpx
from datetime import datetime

from config import config


class EventBusinessModel:

    @staticmethod
    async def get_events():
        """
        Получаем все события

        :return:
        """
        async with httpx.AsyncClient() as client:
            response = await client.get(config["line_provider_url"]+'/event/events')

        response_content = response.text.strip()

        return response_content

    @staticmethod
    async def create_events(coefficient: decimal.Decimal, deadline: datetime):
        """
        Создаем событие

        :return:
        """
        async with httpx.AsyncClient() as client:
            response = await client.post(config["line_provider_url"]+'/event/events', params={"coefficient": coefficient, "deadline": deadline})

        response_content = response.text.strip()

        return response_content
