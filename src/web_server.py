# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = ""
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    '''
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Hello World </title></head>", "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is a simple web server.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))
  '''
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Read the HTML content from the file
        with open('index.html', 'rb') as file:
            html_content = file.read()
        # Set the response body with the HTML content
        self.wfile.write(html_content)

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")