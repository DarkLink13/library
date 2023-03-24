from http.server import SimpleHTTPRequestHandler
from library.controllers import BookController, BaseController

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.controllers: dict[str, BaseController] = {
            'book': BookController(self),
        }
        super().__init__(*args, **kwargs)

    def do_GET(self):
        path_parts = self.path.strip('/').split('/')
        controller_name = path_parts[0]
        controller = self.controllers.get(controller_name)
        if not controller:
            super().do_GET()
            return
        
        if len(path_parts) == 1:
            controller.list()
        elif len(path_parts) == 2 and path_parts[1].isdigit():
            book_id = int(path_parts[1])
            controller.get(book_id)
        elif len(path_parts) == 5 and path_parts[1].isdigit() and path_parts[3].isdigit and path_parts[4] in ('html', 'text'):
            book_id = int(path_parts[1])
            page_number = int(path_parts[3])
            format = path_parts[4]
            if path_parts[2] == 'page':
                controller.get_book_page(book_id, page_number, format)
            else: 
                self.send_response({'error': 'Invalid URL'}, 400)
        else:
            self.send_response({'error': 'Invalid URL'}, 400)