FROM python:3
ENV PYTHONUNBUFFERED 1

ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir -p $APP_HOME
RUN mkdir -p $APP_HOME/sales/staticfiles
RUN mkdir -p $APP_HOME/sales/media
WORKDIR $APP_HOME

ADD . .

RUN pip install -r requirements.txt

RUN chmod +x entrypoint.sh