

import sqlite3
import os

DB_DIR = "nt_storage"
DB_NAME = os.path.join(DB_DIR, "nextrack.db")
SCHEMA_PATH = os.path.join("db_schemas", "sqlite_core.sql")

def init_db(engine_type="sqlite"):
    """
    Initializes the chosen datastore.
    Default is sqlite, but ready for expansion.
    """
    if engine_type == "sqlite":
        _init_sqlite()
    else:
        # This is where you'll plug in other engines later (Postgres, JSON, etc.)
        raise NotImplementedError(f"Engine type '{engine_type}' is not yet supported.")

def _init_sqlite():
    """Private method to handle SQLite-specific setup."""
    if not os.path.exists(DB_DIR):
        os.makedirs(DB_DIR)
        
    conn = sqlite3.connect(DB_NAME)
    if not os.path.exists(SCHEMA_PATH):
        conn.close()
        raise FileNotFoundError(f"Missing schema blueprint at {SCHEMA_PATH}")

    with open(SCHEMA_PATH, 'r') as schemaFile:
        schema_script = schemaFile.read()
    
    conn.executescript(schema_script)
    conn.commit()
    conn.close()

