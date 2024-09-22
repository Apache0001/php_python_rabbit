FROM python:latest

WORKDIR /app

#Cache
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "-u", "consumer.py"]


