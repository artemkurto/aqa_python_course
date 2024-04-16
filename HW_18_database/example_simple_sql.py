import sqlite3
# sql_query = """
# CREATE TABLE IF NOT EXISTS Users (
#     id INTEGER PRIMARY KEY,
#     name TEXT,
#     age INTEGER,
#     email TEXT
# );
# """

sql_query = 'insert into Users values (1, "test_user" , 25, "test@email.com")'

conn = sqlite3.connect(database='test_db.db')
cursor = conn.cursor()
cursor.execute(sql_query)
conn.commit()
cursor.close()
conn.close()
