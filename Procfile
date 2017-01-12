web: gunicorn mysite:mysite -b 0.0.0.0:$PORT -w 10 --log-file -
celery: python mysite/manage.py celeryd --events --loglevel=INFO -c 6 --settings=settings -B
