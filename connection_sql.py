import sqlite3

conn = sqlite3.connect("passwords.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS vault (
    id INTEGER PRIMARY KEY,
    website TEXT,
    username TEXT,
    password TEXT
)
""")

conn.commit()
conn.close()
