import http.server
import socketserver

PORT = 8001

class blog_server(http.server.SimpleHTTPRequestHandler):
   
    def do_GET(self):

        print(self.headers['user-agent'])
        if self.path == "/book":
            filename = 'Python Requests Essentials (en).pdf'
            
            self.send_response(200)
            self.send_header('Content-Type', 'application/pdf')
            # self.send_header('Content-Type', 'application/')
            self.end_headers()
            self.path = filename
        
            return http.server.SimpleHTTPRequestHandler.do_GET(self)


        elif self.path == "/":


            prompt = "Hello World!"
            self.send_response(200)
            self.send_header('Content-Length', '10')
            self.end_headers()
            self.wfile.write(bytes(prompt, 'utf-8'))

    def do_POST(self):
        print('POST REQUEST')
    
        

if __name__ == '__main__':
    print(f'Running on http://localhost:{PORT}')
    my_server = socketserver.TCPServer(("", PORT), blog_server)
    my_server.serve_forever()

# from http.server import HTTPServer, BaseHTTPRequestHandler

# class Serv(BaseHTTPRequestHandler):
#     prompt = ""
#     def do_GET(self):

#         if self.path == '/':
#             prompt = "Hello World!"
#             self.send_response(200)
#         else:
#             prompt = "File not found"
#             self.send_response(404)
#         self.end_headers() #required by BaseHTTPRequestHandler
#         self.wfile.write(bytes(prompt, 'utf-8')) #convert output to bytes and utf-8 is an encoding method


# httpd = HTTPServer(('localhost', 8000), Serv) #Background work, 8000 is the port, localhost is the server
# httpd.serve_forever()


