from http.server import HTTPServer, BaseHTTPRequestHandler

class MiniPy:
    def __init__(self):
        self.routes = {}

    def route(self, path):
        def decorator(func):
            self.routes[path] = func
            return func
        return decorator

    def run(self, host="127.0.0.1", port=8000):

        routes = self.routes

        class RequestHandler(BaseHTTPRequestHandler):

            def do_GET(self):
                if self.path in routes:

                    response = routes[self.path]()

                    self.send_response(200)
                    self.send_header("Content-type", "text/html")
                    self.end_headers()

                    self.wfile.write(response.encode())

                else:
                    self.send_response(404)
                    self.end_headers()
                    self.wfile.write(b"404 Not Found")

        server = HTTPServer((host, port), RequestHandler)
        print(f"MiniPy running on http://{host}:{port}")
        server.serve_forever()
