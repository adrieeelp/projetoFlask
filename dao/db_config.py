import sqlite3
import psycopg2

DB_PATH = "postgresql://neondb_owner:npg_In3CjLKNa1wh@ep-curly-mouse-b771kehk.c-13.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

def get_connection():
    conn = psycopg2.connect(DB_PATH)
    return conn