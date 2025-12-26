import sqlite3

def init_db(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS market_volume (
        timestamp TEXT,
        symbol TEXT,
        price REAL,
        volume REAL,
        source TEXT
    )
    """)
    conn.commit()
    return conn
