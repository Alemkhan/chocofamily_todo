FROM python:3.7-alpine

# set environment variables
ENV PYTHONUNBUFFERED=1 COLUMNS=200 TZ=Asia/Almaty

WORKDIR /app

COPY ./requirements.txt /app
COPY ./.env /app

RUN apk update && \
    apk add bash postgresql-client \
    gcc g++ libc-dev postgresql-dev gettext python3-dev jpeg-dev zlib-dev \
    make git libffi-dev openssl-dev python3-dev \
    libxml2-dev libxslt-dev &&\
    pip install --upgrade pip

RUN pip install -U -r requirements.txt

COPY . /app

# Set timezone
RUN apk add tzdata && \
    ln -fs /usr/share/zoneinfo/Asia/Almaty /etc/localtime && \
    echo "Asia/Almaty" > /etc/timezone && apk del tzdata



ENV TZ=Asia/Almaty
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

EXPOSE 8000
