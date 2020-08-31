import sqlite3

conn = sqlite3.connect(r"../data/chairbot.db")


print("Opened database successfully")

# cursor = con.cursor()
conn.row_factory = lambda cursor, row: row[0]
c = conn.cursor()
last = c.execute('SELECT last FROM cheap').fetchone()
print(last)


# print('SHOWING')
# query = "SELECT last FROM cheap LIMIT 1;"
# results = cursor.execute(query).fetchall()[0].replace("('", '')
# results = cursor.execute(query).fetchone()
# print(results)

conn.commit()
c.close()