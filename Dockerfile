FROM python:3.9.6

RUN pip install fastapi uvicorn pythainlp wheel

EXPOSE 80

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]