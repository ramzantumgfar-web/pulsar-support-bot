import sqlite3
from datetime import datetime

DB = "tickets.db"


def create_ticket(user_id, username, problem):

    db = sqlite3.connect(DB)
    cursor = db.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tickets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        username TEXT,
        problem TEXT,
        date TEXT
    )
    """)

    cursor.execute(
        """
        INSERT INTO tickets
        (user_id, username, problem, date)
        VALUES (?, ?, ?, ?)
        """,
        (
            user_id,
            username,
            problem,
            datetime.now().strftime("%Y-%m-%d %H:%M")
        )
    )

    ticket_id = cursor.lastrowid

    db.commit()
    db.close()

    return ticket_id
