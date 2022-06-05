import datetime
import os
import json
import uuid
import yaml
from enum import Enum

import helpers
from services.telegram import Telegram
from services.database import Database

States = dict(
    STARTED=dict(
        data="",
        complete=True
    ),
    LOCATION=dict(
        data="",
        complete=False
    ),
    ITEM=dict(
        data="",
        complete=False
    ),
    PACKING=dict(
        data="",
        complete=False
    ),
    TYPE=dict(
        data="",
        complete=False
    ),
    PAYMENT=dict(
        data="",
        complete=False
    )
)


class UserStatus(Enum):
    ACTIVE = "ACTIVE"
    BANNED = "BANNED"


class OrderStatus(Enum):
    CLOSED = "CLOSED"
    PENDING = "PENDING"


class User:
    def __init__(self, data):
        self.id = data[0]
        self.status = data[1]
        self.username = data[2]
        self.first_name = data[3]
        self.last_name = data[4]
        self.updated_at = data[5]
        self.created_at = data[6]

    def get(self):
        return self.__dict__


class Order:
    def __init__(self, user_id, data=None):
        if data:
            self.id = data[0]
            self.order_id = data[1]
            self.status = data[2]
            self.state = json.loads(data[3])
            self.created_at = data[4]
            self.updated_at = data[5]
        else:
            self.id = user_id
            self.order_id = uuid.uuid4()
            self.status = OrderStatus.PENDING.value
            self.state = States
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

    def update_state(self, data):
        pass

    def get(self):
        return self.__dict__


# class OrderState(Enum):
#     STARTED = "STARTED"
#     LOCATION = "LOCATION"


class Bot:
    def __init__(self, payload):
        self.id = payload["message"]["from"]["id"]
        self.telegram = Telegram(self.id)
        self.db = Database()
        self.user = self.fetch_user_from_db(payload)
        self.orders = self.fetch_user_orders_from_db()
        self.pending_order = None

    def fetch_user_from_db(self, payload):
        _sql = "SELECT * FROM users WHERE id = '{}'".format(self.id)
        _res = self.db.query_data(_sql)
        _username = ""
        _first_name = ""
        _last_name = ""

        if "username" in payload["message"]["from"]:
            _username = payload["message"]["from"]["username"]

        if "first_name" in payload["message"]["from"]:
            _username = payload["message"]["from"]["first_name"]

        if "last_name" in payload["message"]["from"]:
            _username = payload["message"]["from"]["last_name"]

        if not _res:
            _sql = """
                INSERT INTO users (
                    id,
                    status,
                    username,
                    first_name,
                    last_name,
                    created_at,
                    updated_at
                )
                VALUES (
                    '{id}',
                    '{status}',
                    '{username}',
                    '{first_name}',
                    '{last_name}',
                    '{created_at}',
                    '{updated_at}'
                )   
            """.format(
                id=self.id,
                status=UserStatus.ACTIVE.value,
                username=_username,
                first_name=_first_name,
                last_name=_last_name,
                created_at=datetime.datetime.now(),
                updated_at=datetime.datetime.now())
            # print(_sql)
            self.db.insert_data(_sql)
            _res = self.db.query_data(_sql)

        _user = User(_res[0]).get()
        print("USER >")
        print(_user)
        return _user

    def fetch_user_orders_from_db(self):
        _sql = "SELECT * FROM orders WHERE id = '{}'".format(self.id)
        _res = self.db.query_data(_sql)
        print(_res)

        if _res:
            # if pending orders set pending order flag
            return _res

        return []

    def create_order(self):
        _order = Order(self.id)
        return True

    def route_user(self):
        print("ROUTER")
        # pass user message
        if not self.pending_order:
            self.msg_menu()
        # if order exit => load Order() -> self.pending_order return remainder
        # if no orders return menu

        # if create new order
        #   create an empty order

        pass

    def msg_menu(self):
        _msg = "Hey, check our item menu"
        _keyboard = helpers.get_keyboard("main_menu")
        self.telegram.send_msg(_msg, _keyboard)
        return None


def lambda_handler(event, context):
    print("START PROCESSING >>>")

    # fetching event
    print("EVENT: " + json.dumps(event))
    print(event["body"])
    payload = json.loads(event["body"])
    print(payload)
    print(json.dumps(payload, indent=3))

    # initialize Bot
    bot = Bot(payload)

    # route user
    bot.route_user()
