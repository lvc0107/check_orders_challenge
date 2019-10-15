FROM python:3.7

WORKDIR /app

COPY app.py .

ENTRYPOINT ["python", "app.py"]