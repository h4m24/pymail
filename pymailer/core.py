from pymailer.helpers import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class SensuEvent:

    def __init__(self):
        pass

    def parse_sensu_event(self, eventdata):
        event_check_data = get_event_data(eventdata)
        self.EventId = event_check_data["id"]
        self.EvenAction = event_check_data["action"]
        self.EventTimestamp = event_check_data["timestamp"]
        self.EventOccurences = event_check_data["occurrences"]
        return self.EventId, self.EvenAction, self.EventOccurences, self.EventTimestamp


class SensuEventEmail:
    def __init__(self, email_conf):

        self.EmailSender = email_conf['sender_username']
        self.EmailPassword = email_conf['sender_password']
        self.EmailSubject = email_conf['subject']
        self.EmailRecipient = email_conf['recipient']

    def build_event_email(self, event_properties):
        self.EmailBody = """
        <!DOCTYPE html>
        <html>
        <head>
        <title>Sensu check</title>
        </head>
        <body>
        <table style="width:150%">
          <tr>
            <td>Check Name:</td>
            <td>""" + str(event_properties[0]) + """ </td>
          </tr>
          <tr>
            <td>Check Status:</td>
            <td>""" + str(event_properties[1]) + """</td>
          </tr>
            <tr>
              <td>Instance Name:</td>
              <td>""" + str(event_properties[2]) + """</td>
            </tr>
        </table>
        </body>
        </html>
        """

    def send_event_mail(self):
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
        s.login(self.EmailSender, self.EmailPassword)

        # sendmail function takes 3 arguments: sender's address, recipient's address
        # and message to send - here it is sent as one string.
        s.sendmail(self.EmailSender, self.EmailRecipient, msg.as_string())
        s.quit()
