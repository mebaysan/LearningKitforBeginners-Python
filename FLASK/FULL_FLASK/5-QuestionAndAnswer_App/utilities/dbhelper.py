from flask import g
import sqlite3
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_URL = os.path.join(BASE_DIR, "5-QuestionAndAnswer_App","database.db")
def connect_db():
    conn = sqlite3.connect(DB_URL)
    conn.row_factory = sqlite3.Row
    return conn
def get_db():
    if not hasattr(g,'sqlite3'):
        g.sqlite_db=connect_db()
    return g.sqlite_db

