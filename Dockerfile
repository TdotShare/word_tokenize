FROM python:3.9.6

RUN python -m pip install fastapi uvicorn pythainlp 

EXPOSE 80

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
