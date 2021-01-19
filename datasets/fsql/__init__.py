from os import environ
from urllib.parse import urlparse, parse_qs
from urllib.request import BaseHandler

SQLDIR = environ.get("SQL_DIR", '/var/sql')


class FSQLHandler(BaseHandler):
    def __init__(self):
        self.conn = None

    def fsql_open(self, req):
        _proto, bucket, path, _, query, _rest = urlparse(req.full_url)
        sql_path = SQLDIR + path
        params = parse_qs(query)
        for k, v in params.items():
            if len(v) == 1:
                params[k] = v[0]

        sqlp = open(sql_path, 'r').read()
        sql = str(sqlp).format(**params)
        raise Exception(sql)

        return sql
