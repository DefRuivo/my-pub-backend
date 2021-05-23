FROM python:3.9-buster

ENV PYTHONUNBUFFERED=1
COPY ./commands /commands
COPY . /app
WORKDIR /app

RUN apt-get update && apt-get install -y \
    bash \
    default-libmysqlclient-dev \
    build-essential \
    libffi-dev \
    libjpeg-dev \
    zlib1g-dev \
    libzbar0 \
    python3-dev
RUN pip install --no-cache-dir -r requirements.txt

CMD ["/commands/run-prod.sh"]
