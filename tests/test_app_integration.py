import os
import pytest
from modules.nextrack_dataengine import init_db, DB_DIR

def test_engine_initialization_via_env_variable(monkeypatch):
    """
    Verify that the engine initializes the correct store 
    based on the environment variable set by the launcher.
    """
    # 1. Setup: Use monkeypatch to simulate setting the ENV var in the launcher
    monkeypatch.setenv("NEXTRACK_STORE", "sqlite")
    selected_store = os.getenv("NEXTRACK_STORE")
    
    # 2. Execution: Call init_db with the variable
    # This mimics exactly what ui_main.py will do
    try:
        init_db(selected_store)
        success = True
    except Exception:
        success = False
        
    # 3. Assertion
    assert success is True
    assert os.path.exists(DB_DIR)

def test_engine_raises_error_on_unsupported_store(monkeypatch):
    """
    Verify that an unsupported store name triggers a failure.
    """
    monkeypatch.setenv("NEXTRACK_STORE", "invalid_store")
    selected_store = os.getenv("NEXTRACK_STORE")
    
    with pytest.raises(NotImplementedError):
        init_db(selected_store)
