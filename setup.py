from http.server import HTTPServer
from library import Handler
from os import environ as env

if __name__ == '__main__':
    port = env['SERVER_PORT']
    host = env['SERVER_HOST']
    server = HTTPServer((host, int(port)), Handler)

    print('Server running at http://{}:{}'.format(host, port))

    server.serve_forever()