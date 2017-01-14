web: cd mysite && gunicorn mysite.wsgi:application -b 0.0.0.0:$PORT -w 10 --log-file -
celery: python mysite/manage.py celeryd --events --loglevel=INFO -c 3 --settings=mysite.settings -B
