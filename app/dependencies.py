from database import db
from services import StatisticService


async def get_statistic_service():
    yield StatisticService(db)
