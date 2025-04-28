FROM python:3.13-alpine3.21
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

CMD ["python", "run.py"]
