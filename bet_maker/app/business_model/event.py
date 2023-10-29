import decimal

import httpx
from datetime import datetime


class EventBusinessModel:
    """User's Phone CRUD"""

    def __init__(self):
        self.current_time = datetime.now()
        self.base_url = 'http://line_provider:80'

    async def get_events(self):
        """
        Получаем все события

        :return:
        """
        async with httpx.AsyncClient() as client:
            response = await client.get(self.base_url+'/event/events')

        response_content = response.text.strip()

        return response_content

    async def create_events(self, coefficient: decimal.Decimal, deadline: datetime):
        """
        Создаем событие

        :return:
        """
        async with httpx.AsyncClient() as client:
            response = await client.post(self.base_url+'/event/events', params={"coefficient": coefficient, "deadline": deadline})

        response_content = response.text.strip()

        return response_content
