import streamlit as st
import os
from modules.nextrack_dataengine import init_db

# The logic remains the same!
selected_store = os.getenv("NEXTRACK_STORE", "sqlite")

try:
    init_db(selected_store)
except Exception as e:
    st.error(f"Engine Failure: {e}")
    st.stop()

st.title("NexTrack Dashboard")
# ...
