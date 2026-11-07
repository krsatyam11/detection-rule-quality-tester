import sqlite3
from config.settings import DB_PATH
from utils.logger import logger

def init_db():
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS run_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                total_rules INTEGER,
                total_records INTEGER,
                execution_time REAL
            )
        """)
        conn.commit()
        conn.close()
    except Exception as e:
        logger.error(f"Database init error: {e}")

init_db()