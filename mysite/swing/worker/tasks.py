__author__ = 'Dani'
# from celery.task import periodic_task
# from celery.schedules import crontab
from swing.views import Swing

# @periodic_task(run_every=crontab(hour='6', minute=36))
def runTrends():
    Swing().analyze()
