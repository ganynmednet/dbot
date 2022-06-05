import sqlite3
from sqlite3 import Error

import helpers


class Database:
    def __init__(self):
        self.config = helpers.get_config()
        self.conn = self.create_connection()
        print(r"../db/{}".format(self.config["database"]))

    def create_connection(self):
        """ create a database connection to a SQLite database """
        conn = None
        try:
            conn = sqlite3.connect(r"../db/{}".format(self.config["database"]))
            print(sqlite3.version)
            return conn
        except Error as e:
            print(e)
        # finally:
        #     if conn:
        #         conn.close()

    def insert_data(self, sql):
        """
        Create a new project into the projects table
        :param sql:
        :return: project id
        """

        # sql = ''' INSERT INTO projects(name,begin_date,end_date)
        #           VALUES(?,?,?) '''
        try:
            cur = self.conn.cursor()
            cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)

        return cur.lastrowid

    def query_data(self, sql):
        """
        Query all rows in the tasks table
        :param sql:
        :return:
        """
        cur = self.conn.cursor()
        cur.execute(sql)

        rows = cur.fetchall()

        for row in rows:
            print(row)

        return rows
