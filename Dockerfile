FROM python:3.8

ENV PYTHONUNBUFFERED=1

WORKDIR /statistics_counter
WORKDIR /statistics_counter/app

COPY ./requirements.txt /statistics_counter/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /statistics_counter/requirements.txt

COPY ./app /statistics_counter/app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]