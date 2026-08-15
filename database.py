import sqlite3

DB = "pulsar.db"


def connect():
    return sqlite3.connect(DB)


def add_user(user_id, username):
    db = connect()
    cursor = db.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT
    )
    """)

    cursor.execute(
        "INSERT OR IGNORE INTO users VALUES (?, ?)",
        (user_id, username)
    )

    db.commit()
    db.close()


def get_users_count():
    db = connect()
    cursor = db.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM users"
    )

    count = cursor.fetchone()[0]

    db.close()

    return count
