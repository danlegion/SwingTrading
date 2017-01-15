__author__ = 'Dani'
# from celery.task import periodic_task
# from celery.schedules import crontab

import logging

from celery import Celery
from celery.task import periodic_task
from datetime import timedelta
from os import environ
from swing.views import Swing

REDIS_URL = environ.get('REDISCLOUD_URL', 'redis://localhost')
celery = Celery('tasks', broker=REDIS_URL)

# @periodic_task(run_every=crontab(hour='6', minute=36))
@periodic_task(run_every=timedelta(seconds=10))
def runTrends():

    logging.info(Swing().analyze())
    # Swing().analyze()
