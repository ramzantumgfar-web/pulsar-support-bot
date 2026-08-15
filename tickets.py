import sqlite3
from datetime import datetime

DB = "tickets.db"


def connect():
    return sqlite3.connect(DB)


def setup():
    db = connect()
    cursor = db.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tickets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        username TEXT,
        problem TEXT,
        status TEXT,
        date TEXT
    )
    """)

    db.commit()
    db.close()


def create_ticket(user_id, username, problem):

    db = connect()
    cursor = db.cursor()

    cursor.execute(
        """
        INSERT INTO tickets
        (user_id, username, problem, status, date)
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            user_id,
            username,
            problem,
            "Открыт",
            datetime.now().strftime("%Y-%m-%d %H:%M")
        )
    )

    ticket_id = cursor.lastrowid

    db.commit()
    db.close()

    return ticket_id


def get_user_tickets(user_id):

    db = connect()
    cursor = db.cursor()

    cursor.execute(
        "SELECT * FROM tickets WHERE user_id=?",
        (user_id,)
    )

    tickets = cursor.fetchall()

    db.close()

    return tickets


def close_ticket(ticket_id):

    db = connect()
    cursor = db.cursor()

    cursor.execute(
        """
        UPDATE tickets
        SET status='Закрыт'
        WHERE id=?
        """,
        (ticket_id,)
    )

    db.commit()
    db.close()
