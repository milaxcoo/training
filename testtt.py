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


for i in range(1, 11):
    c.execute("INSERT INTO Users(username, email, age, balance) VALUES (?, ?, ?, ?)", (f'User{i}',
                                                                                       f'ex{i}@gmail.com', i * 10,
                                                                                       1000))


for i in range(0, 11):
    if i % 2 == 0:
        c.execute("UPDATE Users SET balance = ? WHERE id = ?", (500, i + 1))


for i in range(1, 11, 3):
    c.execute("DELETE FROM Users WHERE id = ?", (i,))


c.execute("SELECT username, email, age, balance FROM Users WHERE age != ?", (60,))
users = c.fetchall()
for user in users:
    print(f"Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}")
conn.commit()
conn.close()
