from sqlalchemy import Column, Integer, Date, Numeric

from database import Base


class Statistic(Base):
    __tablename__ = 'statistics'

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False, index=True)
    views = Column(Integer, nullable=True)
    clicks = Column(Integer, nullable=True)
    cost = Column(Numeric(10, 2), nullable=True)
