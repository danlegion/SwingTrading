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

TILL_URL = environ.get("TILL_URL")

@periodic_task(run_every=timedelta(seconds=20))
# @periodic_task(run_every=crontab(hour='6', minute=36))
def runTrends():
    logging.info("Stock analysis started...")
    trends = Swing().analyze()

    for trend in trends:
        news = "Symbol: {0} Advice:{1}".format(trend.symbol, trend.notification)
        logging.info(news)
        if trend.report:
            requests.post(TILL_URL, json={
                "phone": ["14036040747"],
                "text" : news
            })

    logging.info("Stock analysis finished...")

