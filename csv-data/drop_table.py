import sqlite3

connect = sqlite3.connect('test.db')

cursor = connect.cursor()
cursor.execute("DROP TABLE test")
connect.commit()

with open('data_backup.sql', 'r') as query_log:
    query = query_log.read()
    print(query)
    cursor.executescript(query)

connect.execute("DELETE FROM test")
connect.commit()