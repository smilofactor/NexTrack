import pytest
from modules.nextrack_dataengine import init_db
from modules.nextrack_ticketing import create_ticket

def test_create_ticket():
    # 1. Setup: Ensure the database/table exists
    init_db()
    
    # 2. Execution: Create a ticket
    ticket_id = create_ticket("Complete the Showcase Project")
    
    # 3. Assertion: Verify the ticket was created and returned an ID
    assert ticket_id is not None
    assert ticket_id > 0
