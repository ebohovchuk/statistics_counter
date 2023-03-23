import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel


class StatisticRequestSchema(BaseModel):
    date: datetime.date
    views: Optional[int] = None
    clicks: Optional[int] = None
    cost: Optional[Decimal] = None


class AggregateStatisticResponseSchema(BaseModel):
    date: datetime.date
    views: Optional[int] = None
    clicks: Optional[int] = None
    cost: Optional[Decimal] = None
    cpc: Optional[Decimal] = None
    cpm: Optional[Decimal] = None

    class Config:
        orm_mode = True


class StatisticResponseSchema(BaseModel):
    date: datetime.date
    views: Optional[int] = None
    clicks: Optional[int] = None
    cost: Optional[Decimal] = None

    class Config:
        orm_mode = True
