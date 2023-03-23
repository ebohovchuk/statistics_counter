from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import settings

SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOSTNAME}/{settings.POSTGRES_DB}"

engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)

async_session = sessionmaker(bind=engine, class_=AsyncSession, autoflush=False, expire_on_commit=False)

# Base = declarative_base()


# async def init_models():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)

#
# async def get_session() -> AsyncSession:
#     async with async_session() as session:
#         yield session

# class Database:
#     async def get_session(self):
#         async with async_session() as session:
#             yield session
#
#
# async def create_tables():
#     with Database() as db:
#         async with db.get_session() as session:
#             async with session.begin():
#                 await session.run_sync(Base.metadata.create_all)

Base = declarative_base()


class AsyncDatabaseSession:
    def __init__(self):
        self._session = None
        self._engine = None

    def __getattr__(self, name):
        return getattr(self._session, name)

    def init(self):
        self._engine = create_async_engine(
            SQLALCHEMY_DATABASE_URL,
            future=True,
            echo=True,
        )
        self._session = sessionmaker(
            self._engine, expire_on_commit=False, class_=AsyncSession
        )()

    async def create_all(self):
        async with self._engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)


db = AsyncDatabaseSession()
