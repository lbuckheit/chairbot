import sqlite3

con = sqlite3.connect(r"../data/chairbot.db")


print("Opened database successfully")

cursor = con.cursor()

print('SHOWING')
query = "SELECT * FROM listing_history;"
results = cursor.execute(query).fetchall()
print(results)

print('DELETING')
delete_query = 'DELETE FROM listing_history;'
cursor.execute(delete_query)

print('SHOWING')
query = "SELECT * FROM listing_history;"
results = cursor.execute(query).fetchall()
print(results)

print('INSERTING')
update_query = "INSERT INTO listing_history('lastfive') values('[$240 --- https://newyork.craigslist.org/stn/fuo/d/staten-island-steelcase-leap-v2-office/7173662944.html, $245 --- https://newyork.craigslist.org/stn/fuo/d/staten-island-humanscale-freedom/7173667391.html, $240 --- https://newyork.craigslist.org/stn/fuo/d/staten-island-steelcase-think-office/7173707862.html, $280 --- https://newyork.craigslist.org/stn/fuo/d/staten-island-knoll-generation-chair/7170159310.html, $250 --- https://newyork.craigslist.org/que/fuo/d/sunnyside-aeron-office-chair/7179332167.html]');"
cursor.execute(update_query)

print('SHOWING AGAIN')
query = "SELECT * FROM listing_history;"
results = cursor.execute(query).fetchall()

print(results)

a = ['abdjas', 'def', 'ceg']
print(str(a))

con.commit()
cursor.close()