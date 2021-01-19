import urllib.request
from os.path import join
from urllib.parse import urlparse
from urllib.request import BaseHandler


class LocalHandler(BaseHandler):
    pass
    # def unknown_open(self, *req):
    #     raise Exception("yay!")

    # def default_open(self, req, *args, **kwargs):
    #     path = join(req.netloc, req.path).strip("/")
    #     return open(path)
