FROM python:3.9

RUN pip install fastapi uvicorn pythainlp wheel

EXPOSE 80

COPY ./app /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]