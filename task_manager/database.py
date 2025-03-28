import sqlite3
from config import DB_NAME

def get_connection():
    """Create and return a database connection"""
    return sqlite3.connect(DB_NAME)

def create_database():
    """Create the SQLite database and tasks table if they don't exist"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Create tasks table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            task_id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            category TEXT,
            priority INTEGER,
            action_date TEXT,
            deadline TEXT,
            status TEXT NOT NULL,
            estimated_duration INTEGER, 
            real_duration INTEGER,
            last_updated TEXT,
            created_at TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

    print("Database initialized successfully!")
