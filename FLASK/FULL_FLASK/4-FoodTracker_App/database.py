from flask import g
import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_URL = os.path.join(BASE_DIR, "4-FoodTracker_App","food_log.db")

def connect_db():
    sql = sqlite3.connect(DB_URL)
    sql.row_factory = sqlite3.Row
    return sql

def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db