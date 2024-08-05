import sqlite3

conn = sqlite3.connect('not_telegram.db')
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')


c.execute("DELETE FROM Users WHERE id = ?", (6,))

count = c.execute("SELECT count(*) FROM Users")
print(count.fetchone()[0])
sum_balances = c.execute("SELECT sum(balance) FROM Users")
print(sum_balances.fetchone()[0])
avg_balances = c.execute("SELECT avg(balance) FROM Users")
print(avg_balances.fetchone()[0])


conn.commit()
conn.close()
