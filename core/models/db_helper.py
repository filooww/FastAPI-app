from asyncio import current_task
from typing import Any, AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, async_scoped_session

from core.config import settings


class DataBaseHelper:
    def __init__(self, url: str, echo: bool = False):
        self.engine = create_async_engine(
            url = url,
            echo = echo,
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush= False,
            autocommit = False,
            expire_on_commit= False,
        )
    def get_scoped_session(self):
        session = async_scoped_session(
            session_factory=self.session_factory,
            scopefunc= current_task
        )
    async def session_dependency(self) -> AsyncGenerator[Any, Any]:
        async with self.session_factory() as session:
            yield session
            await session.close()

    # Внутри класса DataBaseHelper
    async def scope_session_dependency(self):
        # 1. Создаем сессию через factory
        session = self.session_factory()
        try:
            # 2. ВОТ ТУТ ГЛАВНОЕ: отдаем сессию в FastAPI
            yield session
        finally:
            # 3. Закрываем сессию после выполнения запроса
            await session.close()



db_helper = DataBaseHelper(
    url=settings.DB_URL,
    echo=settings.DB_ECHO
)