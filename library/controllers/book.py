from library.repositories import BookRepository
from library.controllers.base import BaseController
from library.db import conn
import json

formats = { 'html': 'text/html' ,'text': 'text/plain' }

class BookController(BaseController):
    def __init__(self, args):
        self.repository = BookRepository(conn)
        super().__init__(args)

    def list(self):
        books = self.repository.list()
        self.send_response(books)
    
    def get(self, book_id):
        book = self.repository.get_by_id(book_id)
        self.send_response(book)
    
    def get_book_page(self, book_id, page_number, format='html'):
        book = self.repository.get_page_from_book(book_id, page_number)
        if book == None:
            self.send_response({'error': 'Page not Found'}, 404)
            return
        if format in formats:
            self.request_handler.send_response(200)
            self.request_handler.send_header('Content-type', formats[format])
            self.request_handler.end_headers()
            self.request_handler.wfile.write(json.dumps(book).encode("utf-8"))
        else:
            self.send_response({'error': 'Invalid format'}, 400)