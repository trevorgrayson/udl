from os import environ
from urllib.parse import urlparse
from http.client import HTTPSConnection
from urllib.request import BaseHandler

DOMAIN = 'storage.googleapis.com'
GS_TOKEN = environ.get("GS_TOKEN")

# TODO need google certs
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


def headers(token=None):
    h = {
        "Authorization": "Bearer {}".format(GS_TOKEN)
    }
    return h


class GCSHandler(BaseHandler):
    def __init__(self):
        self.conn = HTTPSConnection(DOMAIN)

    def gs_open(self, req, *args, **kwargs):
        proto, bucket, path, *rest = urlparse(req.full_url)
        http_url = "/storage/v1/b/{bucket}/o{path}".format(
            bucket=bucket,
            path=path
        )
        http_url += '?alt=media'
        http_url += '&key=' + GS_TOKEN

        self.conn.request("GET", http_url,
                          headers=headers()
                          )
        resp = self.conn.getresponse()
        if resp.status in [200]:
            return resp
        else:
            raise Exception(f"HTTP Status: {resp.status}:  {resp.headers}")
