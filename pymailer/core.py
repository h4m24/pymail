import helpers
import pymailer

# get the pipe
sensu_event = helpers.get_stdin()

# parse pipe
sensu_event_json = helpers.parse_json(helpers.list_to_string(sensu_event))

# from here On an email will be sent for the event.
email_body = """
<!DOCTYPE html>
<html>
<head>
<title>Sensu check</title>
</head>
<body>
<table style="width:150%">
  <tr>
    <td>Check Name:</td>
    <td>""" + str(sensu_event_json['check']['name']) + """ </td>
  </tr>
  <tr>
    <td>Check Status:</td>
    <td>""" + str(sensu_event_json['check']['status']) + """</td>
  </tr>
    <tr>
      <td>Instance Name:</td>
      <td>""" + str(sensu_event_json['client']['name']) + """</td>
    </tr>
      <tr>
        <td>Check Output:</td>
        <td>""" + str(sensu_event_json['check']['output']) + """</td>
      </tr>
</table>
</body>
</html>
"""

helpers.send_mail('hamza.faouri@zipjet.com','hamza.faouri@zipjet.com',"Sensu Alarm", email_body)