FROM python:3.11

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

EXPOSE 80

CMD ["uvicorn", "app.main:api", "--host", "0.0.0.0", "--port", "80"]