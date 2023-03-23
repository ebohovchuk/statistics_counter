from typing import List, Union

from fastapi import FastAPI, status, Depends

from database import db
from dependencies import get_statistic_service
from exception import GetStatisticException, DeleteStatisticException
from schema import StatisticRequestSchema, AggregateStatisticResponseSchema, StatisticResponseSchema
from services import StatisticService

db.init()

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    await db.create_all()


@app.on_event("shutdown")
async def shutdown():
    await db.close()


@app.get("/statistics", status_code=status.HTTP_200_OK, response_model=List[AggregateStatisticResponseSchema])
async def get_all_statistics(
        from_date: Union[str, None] = None,
        to_date: Union[str, None] = None,
        order_by: Union[str, None] = None,
        statistic_service: StatisticService = Depends(get_statistic_service)
):
    """
    Retrieve and filter all statistics.
    """
    statistic = await statistic_service.get_all_statistics(from_date, to_date, order_by)
    return statistic


@app.post("/statistics", status_code=status.HTTP_201_CREATED, response_model=StatisticResponseSchema)
async def create_statistic(payload: StatisticRequestSchema, statistic_service: StatisticService = Depends(get_statistic_service)):
    """
    Create new statistic.
    """
    statistic = await statistic_service.create(**payload.dict())
    return statistic


@app.delete("/statistics/{id}", status_code=status.HTTP_200_OK)
async def delete_statistic(id: int, statistic_service: StatisticService = Depends(get_statistic_service)):
    """
    Delete the statistic.
    """
    try:
        await statistic_service.delete(id)
    except (GetStatisticException, DeleteStatisticException) as error:
        return {"error_message": error.message}

    return {"message": f"delete statistic item with id {id}"}
