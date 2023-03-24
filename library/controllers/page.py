from library.controllers.base import BaseController
from library.repositories import PageRepository
from library.db import conn

class PageController(BaseController):
    def __init__(self, args):
        self.repository = PageRepository(conn)
        super().__init__(args)

    def list(self):
        pages = self.repository.list()
        self.send_response(pages)
    
    def get(self, page_id):
        page_id = int(self.path.split('/')[2])
        page = self.repository.get_by_book_id(page_id)
        self.send_response(page)