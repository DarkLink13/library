import os
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def get_migrations():
    migrations_dir = os.path.join(os.getcwd(), '.')
    migrations = []
    for filename in os.listdir(migrations_dir):
        if filename.endswith('.sql'):
            migrations.append(filename)
    migrations.sort()
    return migrations


def run_migrations(conn):
    cur = conn.cursor()

    # Create the books table
    cur.execute('''
        CREATE TABLE books (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            author VARCHAR(255) NOT NULL
        )
    ''')

    # Create the pages table
    cur.execute('''
        CREATE TABLE pages (
            number INTEGER NOT NULL,
            text TEXT NOT NULL,
            book_id INTEGER REFERENCES books(id),
            PRIMARY KEY (book_id, number)
        )
    ''')

    conn.commit()
    cur.close()
    conn.close()