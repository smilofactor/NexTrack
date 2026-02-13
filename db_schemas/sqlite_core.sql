-- NexTrack Foundational Schema (SQLite)
CREATE TABLE IF NOT EXISTS tickets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    priority TEXT,
    status TEXT DEFAULT 'Todo',
    origin_node TEXT DEFAULT 'Local'
);
