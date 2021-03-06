__author__ = 'Dani'



import logging

from celery import Celery
from celery.task import periodic_task
from celery.schedules import crontab
from datetime import timedelta
from os import environ
from swing.views import Swing
import requests

REDIS_URL = environ.get('REDISCLOUD_URL', 'redis://localhost')
celery = Celery('tasks', broker=REDIS_URL)
celery.conf.update(
    CELERY_TIMEZONE='Canada/Mountain'
)

TILL_URL = environ.get("TILL_URL")
PHONE_NUMBER = environ.get("PHONE_NUMBER")

# @periodic_task(run_every=timedelta(seconds=20))
@periodic_task(run_every=crontab(hour=21, minute=02, day_of_week='1-5'))
def runTrends():
    logging.info("Stock analysis started...")
    trends = Swing().analyze()

    for trend in trends:
        news = "Symbol: {0} Advice:{1}".format(trend.symbol, trend.notification)
        logging.info(news)
        if trend.report:
            requests.post(TILL_URL, json={
                "phone": [PHONE_NUMBER],
                "text" : news
            })

    logging.info("Stock analysis finished...")
