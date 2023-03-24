import json

class BaseController:
    def __init__(self, request_handler):
        self.request_handler = request_handler
    
    def get(self, id): 
        pass

    def list(self): 
        pass

    def send_response(self, response_data, status_code=200):
        self.request_handler.send_response(status_code)
        self.request_handler.send_header('Content-type', 'application/json')
        self.request_handler.end_headers()
        self.request_handler.wfile.write(json.dumps(response_data).encode('utf-8'))