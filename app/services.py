from datetime import datetime
from typing import Dict, List, Any

from sqlalchemy import Select, func
from sqlalchemy.future import select
from sqlalchemy.sql import between

from constants import DATE_FORMAT, STATISTIC_ORDER_BY
from database import AsyncDatabaseSession
from exception import CreateStatisticException, DeleteStatisticException, GetStatisticException
from models.statistic import Statistic


class StatisticService:
    def __init__(self, db_session: AsyncDatabaseSession):
        self.db_session = db_session

    async def create(self, **kwargs: Dict) -> Statistic:
        statistic = Statistic(**kwargs)
        self.db_session.add(statistic)
        try:
            await self.db_session.commit()
        except Exception as error:
            await self.db_session.rollback()
            raise CreateStatisticException(error)
        return statistic

    async def delete(self, id: int) -> None:
        statistic = await self.get(id)
        await self.db_session.delete(statistic)
        try:
            await self.db_session.commit()
        except Exception as error:
            await self.db_session.rollback()
            raise DeleteStatisticException(error)

    async def get(self, id: int) -> Statistic:
        query = select(Statistic).where(Statistic.id == id)
        statistics = await self.db_session.execute(query)
        statistic = statistics.scalar_one_or_none()
        if not statistic:
            raise GetStatisticException(f"Statistic item with id {id} does not exist")
        return statistic

    def _get_query(self, from_date: str, to_date: str, order_by: str) -> Select[Any]:
        from_date = datetime.strptime(from_date, DATE_FORMAT) if from_date else None
        to_date = datetime.strptime(to_date, DATE_FORMAT) if to_date else None

        query = select(
                Statistic.date,
                func.sum(Statistic.views).label('views'),
                func.sum(Statistic.clicks).label('clicks'),
                func.sum(Statistic.cost).label('cost'),
                (func.avg(Statistic.cost / Statistic.clicks)).label('cpc'),
                ((func.avg(Statistic.cost / Statistic.views)) * 1000).label('cpm')
            ).group_by(Statistic.date)

        if from_date and to_date:
            query = query.filter(between(Statistic.date, from_date, to_date))
        elif from_date:
            query = query.filter(Statistic.date >= from_date)
        elif to_date:
            query = query.filter(Statistic.date <= to_date)

        if order_by in STATISTIC_ORDER_BY:
            query = query.order_by(STATISTIC_ORDER_BY.get(order_by))
        else:
            query = query.order_by(Statistic.date)

        return query

    async def get_all_statistics(self, from_date: str = None, to_date: str = None, order_by: str = None) -> List[Statistic]:
        query = self._get_query(from_date, to_date, order_by)
        statistics = await self.db_session.execute(query)
        return statistics.fetchall()
