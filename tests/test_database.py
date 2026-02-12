
import os
import shutil
from modules.database import init_db, DB_DIR, DB_NAME

def test_init_db_creates_directory_and_file():
    # 1. Setup: Completely remove the data directory to simulate a fresh install
    if os.path.exists(DB_DIR):
        shutil.rmtree(DB_DIR)
    
    # 2. Execution
    init_db()
    
    # 3. Assertions
    assert os.path.exists(DB_DIR), f"{DB_DIR} directory was not created"
    assert os.path.isdir(DB_DIR), f"Path {DB_DIR} is not a directory"
    assert os.path.exists(DB_NAME), f"{DB_NAME} was not created inside {DB_DIR}"
