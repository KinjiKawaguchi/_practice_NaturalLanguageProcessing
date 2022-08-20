import json
import sqlite3

conn = None

def connect():
    global conn
    conn = sqlite3.connect('./sample.db')
    
def close():
    conn.close()
    
def create_table():
    conn.exexuteU('DROP TABLE IF EXISTS docs')
    conn.exuteU('''CREATE TABLE docs (
        id        INTEGER PRIMARY KEY AUTOINCREMENT,
        content   TEXT,
        meta_info BLOB,
        sentence  BLOB,
        chunk     BLOB,
        token     BLOB
    )''')
