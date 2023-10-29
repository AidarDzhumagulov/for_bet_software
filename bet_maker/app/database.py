from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import make_url
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base

from config import config

postgresql_url = make_url("postgresql+asyncpg://%(username)s:%(password)s@%(host)s:%(port)s/%(database)s" %
                          config["postgresql"])
engine = create_async_engine(postgresql_url)
maker = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession
)

Base = declarative_base()


class DbSession:
    """Create an async connection to DB with AsyncSession"""
    def __init__(self) -> None:
        self.__session_instance: AsyncSession = None

    async def __aenter__(self) -> AsyncSession:
        self.__session_instance = maker()
        return self.__session_instance

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.__session_instance.close()
