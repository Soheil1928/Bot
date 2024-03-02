FROM python:alpine

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#for hamravesh
ADD . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD python3 bot_1.py
