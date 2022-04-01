import os
import sqlite3


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except :
        pass

def db_create_connection(db_file: str):
    """Create a connection to a SQLite database

    Arguments:
        db_file {str} -- Full path and file name

    Returns:
        conn -- Returns a connection object or None
    """

    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as Error:
        print(f"ERROR: {Error}")
        return None

    return conn


def db_select_all_rows(conn, sql):
    """Select all rows from the selected database & table using the provided SQL statement.
       It returns a rowset or None

    Arguments:
        conn {conn} -- Existing database connection
        sql {str} -- SQL statement to execute
    """
    cur = conn.cursor()
    try:
        cur.execute(sql)
    except sqlite3.Error as Error:
        print(f"ERROR: {Error}")
        return None

    rows = cur.fetchall()

    if rows:
        return rows
    else:
        return None


def db_execute_sql(conn, list_sql):
    """Select all rows from the selected database & table using the provided SQL statement.
       It returns a rowset or None

    Arguments:
        conn {conn} -- Existing database connection
        sql {str} -- SQL statement to execute
    """
    cur = conn.cursor()
    for idx, sql in enumerate(list_sql):
        try:
            cur.execute(sql)

        except sqlite3.Error as Error:
            print(f"ERROR: {Error}")
            return cur
    if idx == len(list_sql) - 1:
        cur.close()


def db_execute_sql_fetchall(conn, sql):
    """Select all rows from the selected database & table using the provided SQL statement.
       It returns a rowset or None

    Arguments:
        conn {conn} -- Existing database connection
        sql {str} -- SQL statement to execute
    """
    cur = conn.cursor()
    try:
        cur.execute(sql)
        rows = cur.fetchall()
    except sqlite3.Error as Error:
        print(f"ERROR: {Error}")
        return None

    return rows



def folders_check(folder_name: str, create: bool):
    """Check the existence of a folder and optionally creating it, if it doesn't exist

    Arguments:
        folder_name {str} -- Folder to check
        create {boolean} -- True / False: Create it or not if it doesn't exist

    Returns:
        Boolean -- True or False
    """

    exists = False

    if not os.path.exists(folder_name):

        if create:
            try:
                os.makedirs(folder_name)
                exists = True
            except Exception as Err:
                print(Err)
    else:
        exists = True

    return exists

