from library.db import conn

def run_seeds():
    cur = conn.cursor()

    cur.execute("INSERT INTO books (title, author) VALUES (%s, %s)", ('The Great Gatsby', 'F. Scott Fitzgerald'))
    cur.execute("INSERT INTO books (title, author) VALUES (%s, %s)", ('To Kill a Mockingbird', 'Harper Lee'))
    cur.execute("INSERT INTO books (title, author) VALUES (%s, %s)", ('1984', 'George Orwell'))
    conn.commit()

    cur.execute("INSERT INTO pages (number, text, book_id) VALUES (%s, %s, %s)", (1, 'In my younger and more vulnerable years...', 1))
    cur.execute("INSERT INTO pages (number, text, book_id) VALUES (%s, %s, %s)", (2, 'I was halfway across America...', 1))
    cur.execute("INSERT INTO pages (number, text, book_id) VALUES (%s, %s, %s)", (3, 'So we compromised that I was to go west...', 1))
    cur.execute("INSERT INTO pages (number, text, book_id) VALUES (%s, %s, %s)", (1, 'When he was nearly thirteen, my brother...', 2))
    cur.execute("INSERT INTO pages (number, text, book_id) VALUES (%s, %s, %s)", (2, 'Jem, the older child...', 2))
    cur.execute("INSERT INTO pages (number, text, book_id) VALUES (%s, %s, %s)", (3, 'As the summer progressed...', 2))
    cur.execute("INSERT INTO pages (number, text, book_id) VALUES (%s, %s, %s)", (1, 'It was a bright cold day', 3))
    conn.commit()