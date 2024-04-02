from lib.smtpd_auth import SMTPServer, SMTPChannel, CredentialValidator
import asyncore
import config
import tasks

class RelaySMTPChannel(SMTPChannel):
    def __init__(self, server, conn, addr, *args, **kwargs):
        self.fqdn = config.RELAY_FQDN
        self.hello_msg = "Welcome to Simple SMTP Relay ESMTP Server!"
        super().__init__(server, conn, addr, *args, **kwargs)

class RelayCredentialValidator(CredentialValidator):
    def validate(self):
        for cred in config.VALID_RELAY_ACCOUNTS:
            if self.username == cred["username"] and self.password == cred["password"]:
                return True
        return False

class RelaySMTPServer(SMTPServer):
    credential_validator = RelayCredentialValidator
    channel_class = RelaySMTPChannel

    def process_message(self, peer, mailfrom, rcpttos, data, **kwargs):
        tasks.send_email.delay(mailfrom, rcpttos, data)

RelaySMTPServer(
    config.RELAY_HOST,
    None
)

while True:
    try:
        print("Starting relay server...")
        asyncore.loop(15)
    except KeyboardInterrupt:
        print("Shutting down...")
        break
