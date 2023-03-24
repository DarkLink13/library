from library.models import Page
from library.repositories.base import BaseRepository

class PageRepository(BaseRepository):
    def __init__(self, conn):
        self.conn = conn

    def __del__(self):
        self.conn.close()

    def get_by_book_id(self, book_id, page_number):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM pages WHERE book_id = %s AND number = %s", (book_id, page_number))
        page = cur.fetchone()
        cur.close()
        if page:
            return Page(page[2], page[3], page[4]).to_dict()
        return None
    
    def list(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM pages")
        pages = []
        for page in cur.fetchall():
            pages.append(Page(page[1], page[2], page[3]).to_dict())
        cur.close()
        return pages