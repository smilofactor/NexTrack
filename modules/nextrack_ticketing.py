import sqlite3
from modules.nextrack_dataengine import DB_NAME

def create_ticket(title, priority="Medium"):
    """Inserts a new ticket into the database and returns the ticket ID."""
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tickets (title, priority) VALUES (?, ?)", 
            (title, priority)
        )
        conn.commit()
        ticket_id = cursor.lastrowid
        conn.close()
        return ticket_id
    except sqlite3.OperationalError:
        # If the table doesn't exist yet, return None to trigger the test failure
        return None
