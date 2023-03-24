class Page:
    def __init__(self, number, text, book_id):
        self.number = number
        self.text = text
        self.book_id = book_id

    def to_dict(self):
        return { 'number': self.number, 'text': self.text, 'book_id': self.book_id }