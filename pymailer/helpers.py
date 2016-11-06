import json
import argparse


def parse_alerter_arguments(arguments_list):
    parser = argparse.ArgumentParser()
    return parser.parse_args()


def read_alerter_conf_file(conf_file_path):
    # open file read contents and return attributes
    with open(conf_file_path) as conf_file:
        return json.load(conf_file)


def get_event_data(eventdata):
    return json.loads(eventdata)




#
# def check_stash():
#     # read sensu stash
#     sensu_api_stashes = urllib2.urlopen("http://localhost:4567/stashes").read()
#
#     #  list stashes
#     sensu_api_stashes_json = parse_json(helpers.list_to_string(sensu_api_stashes))
#
#     # get silent event path
#     sensu_silent_event_path = "silence/" + sensu_event_json['client']['name'] + "/" + sensu_event_json['check']['name']
#
#     # check if server is silenced
#     for stash_entry in sensu_api_stashes_json:
#         if sensu_silent_event_path == stash_entry['path']:
#             sys.exit(0)
#
#
#
#
# def parse_json(input_string):
#     return json.loads(input_string)

#
# print get_event_data_from_stdin()["occurrences"]
