import cgi
from http.server import HTTPServer, BaseHTTPRequestHandler

tasklist = ['Create a Web Server',
            'Implement a Load Balancer',
            'Create Virtual IP Address for Load Balancer',
            'Implement Firewall',
            'Prevent Security Attacks',
            'Assess Performance Metrics']

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if(self.path.endswith('/tasklist')):
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()

            response = ''
            response += '<html><body>'
            response += '<h1>Computer Networks</h1>'
            response += '<h2>Task list</h2>'
            response += '<h3><a href="/tasklist/new">Add New Task</a></h3>'
            for task in tasklist:
                response += '<p> &bull; %s' % task + '    '
                response += '<a href="/tasklist/%s/remove">remove</a>' % task
                response += '</p></br>'
            response += '</body></html>'
            self.wfile.write(response.encode())

        if(self.path.endswith('/new')):
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()

            response = ''
            response += '<html><body>'
            response += '<h1>Add New Task</h1>'
            response += '<form method="POST" enctype="multipart/form-data" action="/tasklist/new">'
            response += '<input name="task" type="text" placeholder="Add new task">'
            response += '<input type = "submit" value="Add">'
            response += '</form>'
            response += '</body></html>'
            self.wfile.write(response.encode())

        if self.path.endswith('/remove'):
            listIDPath = self.path.split('/')[2]
            print(listIDPath)
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()

            response = ''
            response += '<html><body>'
            response += '<h1>Remove Task: %s</h1>' % listIDPath.replace('%20', ' ')
            response += '<form method="POST" enctype="multipart/form-data" action="/tasklist/%s/remove">' % listIDPath
            response += '<input type = "submit" value="Remove"></form>'
            response += '<h3><a href="/tasklist">Cancel</a></h3>'
            response += '</body></html>'
            self.wfile.write(response.encode())

    def do_POST(self):
        if(self.path.endswith('/new')):
            ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
            pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
            content_length = int(self.headers.get('Content-length'))
            pdict['CONTENT-LENGTH'] = content_length
            if(ctype == 'multipart/form-data'):
                fields = cgi.parse_multipart(self.rfile, pdict)
                new_task = fields.get('task')
                tasklist.append(new_task[0])

            self.send_response(301)
            self.send_header('Content-type', 'text/html')
            self.send_header('Location', '/tasklist')
            self.end_headers()

        if self.path.endswith('/remove'):
            listIdPath = self.path.split('/')[2]
            ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
            if (ctype == 'multipart/form-data'):
                list_item = listIdPath.replace('%20', ' ')
                tasklist.remove(list_item)

            self.send_response(301)
            self.send_header('Content-type', 'text/html')
            self.send_header('Location', '/tasklist')
            self.end_headers()




def main():
    port = 9000
    server_address = ('localhost', port)
    server = HTTPServer(server_address, HelloHandler)
    print('Server running on port %s' % port)
    server.serve_forever()


# if __name__ == '__main__':
#     main()
