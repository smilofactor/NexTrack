
import sqlite3
import os

# Define the path to the data directory
DB_DIR = "nt_storage"
DB_NAME = os.path.join(DB_DIR, "nextrack.db")

def init_db():
    """Initialize the localized SQLite database in the data directory."""
    # Ensure the directory exists
    if not os.path.exists(DB_DIR):
        os.makedirs(DB_DIR)
        
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
