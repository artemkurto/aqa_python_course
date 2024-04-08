from HW_18_data_base.db_base.sql_connector import SqliteConnector


def execute_sql_query(fn):
    def wrapper(*args, **kwargs):
        with SqliteConnector() as cursor:
            return cursor.execute(fn(*args, **kwargs)).fetchall()

    return wrapper


