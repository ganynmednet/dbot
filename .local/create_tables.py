import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = r"../db/temp.db"

    sql_create_users_table = """ CREATE TABLE IF NOT EXISTS users (
                                        id integer PRIMARY KEY,
                                        status text NOT NULL,
                                        username text,
                                        first_name text,
                                        last_name text,
                                        created_at text,
                                        updated_at text
                                    ); """

    sql_create_orders_table = """ CREATE TABLE IF NOT EXISTS orders (
                                        id integer PRIMARY KEY,
                                        order_id text NOT NULL,
                                        state text NOT NULL,
                                        status text NOT NULL,
                                        created_at text,
                                        updated_at text
                                    ); """



    # sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
    #                                 id integer PRIMARY KEY,
    #                                 name text NOT NULL,
    #                                 priority integer,
    #                                 status_id integer NOT NULL,
    #                                 project_id integer NOT NULL,
    #                                 begin_date text NOT NULL,
    #                                 end_date text NOT NULL,
    #                                 FOREIGN KEY (project_id) REFERENCES projects (id)
    #                             );"""

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create users table
        create_table(conn, sql_create_users_table)

        # create states table
        create_table(conn, sql_create_orders_table)
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
