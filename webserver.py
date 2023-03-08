import http.server
import socketserver

PORT=8815

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("",PORT), Handler) as httpd:
    print("Server is running at Port", PORT)
    print("To test from dockerised version, please run http://localhost:<exposed_port>")
    httpd.serve_forever()