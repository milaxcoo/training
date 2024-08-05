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

counter = c.execute("SELECT count(*) FROM Users")
count = counter.fetchone()[0]
print("Количество записей: ", count)
sum_balances = c.execute("SELECT sum(balance) FROM Users")
summ = sum_balances.fetchone()[0]
print("Сумма балансов: ", summ)
print("Средний баланс: ", summ/count)


conn.commit()
conn.close()
