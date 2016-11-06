from pymailer.facade import *


def main(arguments_list, event_data):
    """ this will be using the Facade which is Alerter CLass"""

    alerter = SensuAlerter()

    try:
        # parse argv
        # create an object from facade class and let it parse arguments
        alerter.read_alerter_arg(arguments_list)
    except IOError:
        print("failed to read arguemnts")

    try:
        # read conf
        # create an object from facade class and let it read configs
        alerter_config = alerter.read_alerter_config()
    except IOError:
        print("failed to read script configs")

    try:
        # process event
        event_properties = alerter.process_sensu_event(event_data)
    except Exception:
        print("failed to parse sensu event")

    # try:
        # send mail
        # create an object from facade class and let it send mail
        # this is expecting event properties, email config from alerter file
    alerter.send_alerter_mail(alerter_config, event_properties)
    # except Exception:
    #     print("failed to send mail")
