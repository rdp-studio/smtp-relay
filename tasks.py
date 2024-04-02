from celery import Celery
import config
import smtplib

app = Celery("tasks", broker=config.CELERY_BROKER)

@app.task
def send_email(mailfrom, rcpttos, data):
    if config.UPSTREAM_SSL:
        uplib = smtplib.SMTP_SSL
    else:
        uplib = smtplib.SMTP
    with uplib(config.UPSTREAM_SERVER[0], config.UPSTREAM_SERVER[1]) as server:
        server.login(config.UPSTREAM_USERNAME, config.UPSTREAM_PASSWORD)
        server.sendmail(mailfrom, rcpttos, data)
        return
