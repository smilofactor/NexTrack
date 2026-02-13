
import sqlite3
import os

# Define the path to the data directory
DB_DIR = "nt_storage"
DB_NAME = os.path.join(DB_DIR, "nextrack.db")
# Path to SQL schema no storage hard coding
SCHEMA_PATH = os.path.join("db_schemas", "sqlite_core.sql")

def init_db():
    """Initialize the localized SQLite database in the data directory."""
    # Ensure the directory exists
    if not os.path.exists(DB_DIR):
        os.makedirs(DB_DIR)
        
    conn = sqlite3.connect(DB_NAME)

    # Senior Touch: Ensure the schema file actually exists before reading
    if not os.path.exists(SCHEMA_PATH):
        conn.close()
        raise FileNotFoundError(f"Missing schema blueprint at {SCHEMA_PATH}")

    with open(SCHEMA_PATH, 'r') as schemaFile:
        schema_script = schemaFile.read()

    conn.executescript(schema_script)
    conn.commit()
    conn.close()
