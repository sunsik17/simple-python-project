import sqlite3

product_list = [
    [1, '모자', 30000],
    [2, '스니커즈', 50000],
    [3, '청바지', 100000],
    [4, '티셔츠', 29000]
]

connect = sqlite3.connect('test.db')
cursor = connect.cursor()

cursor.executemany("INSERT OR REPLACE INTO test(id, product_name, price) values(?, ?, ?)", product_list)
connect.commit()

for line in connect.iterdump():
    print(line)

with connect:
    with open('data_backup.sql', 'w') as f:
        for line in connect.iterdump():
            f.write('%s\n' % line)
        print('Completed')

