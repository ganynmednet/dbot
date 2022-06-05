import json
import os

import main as main


def run():
    with open('payload.json', "r", encoding="utf8") as json_file:
        merchant = json.load(json_file)
    os.environ["ENV"] = "dev"
    print(main.lambda_handler(merchant, "hey"))


run()
