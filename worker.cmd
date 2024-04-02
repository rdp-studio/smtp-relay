@poetry run celery -A tasks worker -P eventlet -c 4 --loglevel=INFO
