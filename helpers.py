import os
import yaml
import json


def get_config():
    # fetching config
    with open("{}/config.yml".format(os.path.dirname(os.path.realpath(__file__))), 'r') as stream:
        _config = yaml.safe_load(stream)
    return _config[os.environ["ENV"]]


def get_keyboard(name):
    print("GETTING CONFIG >>>")
    with open(os.path.dirname(__file__) + "/services/src/{}.json".format(name), "r", encoding="utf8") as read_file:
        _keyboard = json.load(read_file)
        read_file.close()
    return _keyboard
