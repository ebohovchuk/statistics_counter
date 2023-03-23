from sqlalchemy import func

from models.statistic import Statistic

DATE_FORMAT = "%Y-%m-%d"

STATISTIC_ORDER_BY = {
    "views": func.sum(Statistic.views),
    "clicks": func.sum(Statistic.clicks),
    "cost": func.sum(Statistic.cost),
    "cpc": func.avg(Statistic.cost / Statistic.clicks),
    "cpm": func.avg(Statistic.cost / Statistic.views),
}