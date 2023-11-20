import sqlite3

conn = sqlite3.connect('test.db')
c = conn.cursor()
query = '''CREATE TABLE if not exists test (ID INTEGER PRIMARY KEY, PRODUCT_NAME TEXT, PRICE INTEGER)'''
c.execute(query)
c.execute('''SELECT * FROM sqlite_master WHERE type="table"''')
print(c.fetchall())
q = '''INSERT INTO test(product_name, price) values ('가방', 3000)'''
c.execute(q)
conn.commit()
c.execute('''DELETE FROM test''')
conn.commit()
product_list = [
    ['모자', 15000],
    ['가방', 200000],
    ['후드티', 99000]
]
c.executemany('''INSERT INTO test(product_name, price) values (?, ?)''', product_list)
conn.commit()

c.execute("UPDATE test SET (PRODUCT_NAME, PRICE)= ('%s', '%s') WHERE Id = '%s'" % ('핸드폰', 1000000, 2))
conn.commit()

c.execute("DELETE FROM test WHERE id =?", (3,))
conn.commit()

c.execute("DELETE FROM test WHERE PRODUCT_NAME = :product_name", {'product_name':'핸드폰'})
conn.commit()

c.execute("DELETE FROM test")
conn.commit()
conn.close()
