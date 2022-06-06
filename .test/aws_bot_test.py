import json
import os

import main as main


def run():

    with open('payload.json', "r", encoding="utf8") as json_file:
        T_1 = json.load(json_file)

    with open('locations.json', "r", encoding="utf8") as json_file:
        T_2 = json.load(json_file)

    with open('items.json', "r", encoding="utf8") as json_file:
        T_3 = json.load(json_file)

    os.environ["ENV"] = "dev"
    print(main.lambda_handler(T_1, "hey"))


run()
