poetry run celery -A tasks worker -c 4 --loglevel=INFO
