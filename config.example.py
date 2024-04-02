# 上游配置
UPSTREAM_SSL = True
UPSTREAM_SERVER = ("smtp.sendgrid.net", 465)
UPSTREAM_USERNAME = "apikey"
UPSTREAM_PASSWORD = ""

# 队列配置
CELERY_BROKER = ""

# relay配置
RELAY_FQDN = "relay.internal"
RELAY_HOST = ("0.0.0.0", 25)

# 账号配置
VALID_RELAY_ACCOUNTS = [
    {
        "username": "test",
        "password": "test"
    }
]
