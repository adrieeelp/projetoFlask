import sqlite3

DB_PATH = "banco_escola_pweb2.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    return conn