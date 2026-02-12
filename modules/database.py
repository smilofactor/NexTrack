import sqlite3

DB_NAME = "nextrack.db"

def init_db():
    """Initialize the localized SQLite database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            priority TEXT,
            status TEXT DEFAULT 'Todo',
            origin_node TEXT DEFAULT 'Local'
        )
    ''')
    conn.commit()
    conn.close()
