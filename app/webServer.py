import tornado.web
import os

class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(f"Served from {os.getpid()}")




# if __name__ == "__main__":
#     tornado.web.Application([()])
