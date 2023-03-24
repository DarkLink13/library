from library.models import Book, Page

class BookRepository:
    def __init__(self, conn):
        self.conn = conn

    def __del__(self):
        self.conn.close()

    def get_page_from_book(self, book_id, page_number):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM pages WHERE book_id = %s AND number = %s", (book_id, page_number))
        page = cur.fetchone()
        cur.close()
        if page:
            return Page(page[0], page[1], page[2]).to_dict()
        return None
    
    def get_by_id(self, book_id):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM books WHERE id = %s", (book_id,))
        book = cur.fetchone()
        cur.close()
        if book:
            return Book(book[1], book[2]).to_dict()
        return None

    def list(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM books")
        books = []
        for book in cur.fetchall():
            books.append(Book(book[1], book[2]).to_dict())
        cur.close()
        return books