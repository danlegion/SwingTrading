web: newrelic-admin run-program gunicorn mysite.wsgi -b 0.0.0.0:$PORT -w 10
celery: python mysite/manage.py celeryd --events --loglevel=INFO -c 6 --settings=settings -B
