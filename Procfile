web: cd mysite && gunicorn mysite.wsgi:application -b 0.0.0.0:$PORT -w 10 --log-file -
celery: cd mysite && celery -A swing.worker.tasks worker -B --loglevel=info --events
