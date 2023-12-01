FROM python:3.11-alpine

WORKDIR /app

COPY . /app


RUN pip install -r /app/requirements.txt


CMD ["python", "products_api.py"]