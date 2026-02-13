
import os
import shutil
import sqlite3
import pytest
from modules.nextrack_dataengine import init_db, DB_DIR, DB_NAME, SCHEMA_PATH

def test_init_db_creates_everything():
    """Verify that init_db creates the directory, the file, and the schema."""
    # 1. Setup: Clean slate
    if os.path.exists(DB_DIR):
        shutil.rmtree(DB_DIR)

    # 2. Pre-condition check: Does the schema file exist where we expect it?
    assert os.path.exists(SCHEMA_PATH), f"Schema file missing at {SCHEMA_PATH}"

    # 3. Execution
    init_db()

    # 4. Assertions
    # Check physical file existence
    assert os.path.exists(DB_NAME), "Database file was not created"

    # Check internal structure (Did the SQL actually run?)
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    # Query the sqlite_master table to see if our 'tickets' table exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='tickets';")
    table_exists = cursor.fetchone()
    conn.close()

    assert table_exists is not None, "Table 'tickets' was not found in the database"
