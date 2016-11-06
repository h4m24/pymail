import smtplib
from  helpers import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class SensuAlerter:
    def __init__(self):
        # read alerter config
        pass

    def get_sensu_event(self):
        # call sensu event class
        sensu_event = SensuEvent
        print sensu_event.EventId
        pass

    def send_alert_email(self):
        # call sensu email class
        pass


# class SensuAlerterConfig:
#
#     def __init__(self):
#         pass
#
#     def read_config_file(self):
#         pass


class SensuEvent:
    def __init__(self):
        self.EventId = get_event_data_from_stdin()["id"]
        self.EventAction = get_event_data_from_stdin()["action"]
        self.EventTimestamp = get_event_data_from_stdin()["timestamp"]
        self.EventOccurrences = get_event_data_from_stdin()["occurrences"]


class EventEmail:
    def __init__(self, email_subject, email_recipient, email_body, email_sender):
        self.EmailSubject = email_subject
        self.EmailRecipient = email_recipient
        self.EmailBody = email_body
        self.EmailSender = email_sender

    def get_email_configs(self):
        pass
        # read config from helper function

    def send_mail(self):
        # Create message container - the correct MIME type is multipart/alternative.
        msg = MIMEMultipart('alternative')
        msg['Subject'] = self.EmailSubject
        msg['From'] = self.EmailSender
        msg['To'] = self.EmailRecipient

        # Attach parts into message container.
        # According to RFC 2046, the last part of a multipart message, in this case
        # the HTML message, is best and preferred.
        msg.attach(MIMEText(self.EmailBody, 'html'))

        # Send the message via local SMTP server.
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.ehlo()
        s.starttls()
        s.login('hamza.faouri@zipjet.com', 'password')

        # sendmail function takes 3 arguments: sender's address, recipient's address
        # and message to send - here it is sent as one string.
        s.sendmail(self.EmailSender, self.EmailRecipient, msg.as_string())
        s.quit()
