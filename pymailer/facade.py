from pymailer.helpers import *
from pymailer.core import *


class SensuAlerter:

    pymailer_conf_path = './pymailer.json'

    def __init__(self):
        # what is there to initialize
        pass

    def read_alerter_arg(self, arguments_list):
        # call the arguments parser function from helpers
        parse_alerter_arguments(arguments_list)

    def read_alerter_config(self):
        # call the config file reader function/class?
        read_alerter_conf_file(self.pymailer_conf_path)
        pass

    def process_sensu_event(self, eventdata):
        # read and parse the event data
        event = SensuEvent()
        event.parse_sensu_event(eventdata)
        pass

    def send_alerter_mail(self, ):
        # call the email sender function/class?

        pass
