from flask import g
import sqlite3
import psycopg2
from psycopg2.extras import DictCursor

def connect_db():
    conn = psycopg2.connect('postgres://tvhzjbmbixrooq:f059d79e94325985b38602916994ceb05e6fc851f64dd182bc19bd0995916fa7@ec2-50-19-83-146.compute-1.amazonaws.com:5432/d2qivrch116vtm', cursor_factory=DictCursor)
    conn.autocommit = True
    sql = conn.cursor()
    return conn, sql

def get_db():
    db = connect_db()

    if not hasattr(g, 'postgres_db_conn'):
        g.postgres_db_conn = db[0]

    if not hasattr(g, 'postgres_db_cur'):
        g.postgres_db_cur = db[1]

    return g.postgres_db_cur

def init_db():
    db = connect_db()

    db[1].execute(open('schema.sql', 'r').read())
    db[1].close()

    db[0].close()

def init_admin():
    db = connect_db()

    db[1].execute('update users set admin = True where name = %s', ('admin', ))

    db[1].close()
    db[0].close()