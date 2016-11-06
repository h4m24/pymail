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









#
# # get the pipe
# sensu_event = helpers.get_stdin()
#
# # parse pipe
# sensu_event_json = helpers.parse_json(helpers.list_to_string(sensu_event))
#
# # from here On an email will be sent for the event.
# email_body = """
# <!DOCTYPE html>
# <html>
# <head>
# <title>Sensu check</title>
# </head>
# <body>
# <table style="width:150%">
#   <tr>
#     <td>Check Name:</td>
#     <td>""" + str(sensu_event_json['check']['name']) + """ </td>
#   </tr>
#   <tr>
#     <td>Check Status:</td>
#     <td>""" + str(sensu_event_json['check']['status']) + """</td>
#   </tr>
#     <tr>
#       <td>Instance Name:</td>
#       <td>""" + str(sensu_event_json['client']['name']) + """</td>
#     </tr>
#       <tr>
#         <td>Check Output:</td>
#         <td>""" + str(sensu_event_json['check']['output']) + """</td>
#       </tr>
# </table>
# </body>
# </html>
# """
#
# helpers.send_mail('hamza.faouri@zipjet.com','hamza.faouri@zipjet.com',"Sensu Alarm", email_body)