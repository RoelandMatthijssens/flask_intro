import sqlite3
from flask import g
from flask_intro import app
from flask.cli import with_appcontext
import click

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect('database')
        g.db.row_factory = sqlite3.Row
    return g.db

def init_db():
    db = get_db()
    with app.open_resource('schema.sql') as schema:
        db.executescript(schema.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    print('Initialized the db')

def query(query_string, args=(), one=False):
    db = get_db()
    cursor = db.execute(query_string, args)
    results = cursor.fetchall()
    db.commit()
    cursor.close()
    return (results[0] if results else None) if one else results
