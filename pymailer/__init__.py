from pymailer import *


def main():
    # instantiate alerter object
    alerter = SensuAlerter()
    # alerter.read_config_file()
    # read input
    alerter.get_sensu_event()
    # send email
    # alerter.send_alert_email


if __name__ == '__main__':
    main()
