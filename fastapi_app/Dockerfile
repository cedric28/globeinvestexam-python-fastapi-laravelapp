# fastapi_app/Dockerfile

FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

WORKDIR /app

COPY ./app /app
COPY ../sales_data.db /app/sales_data.db  # Copy the SQLite database file

RUN pip install pandas

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
