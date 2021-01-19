import datasets
from datasets import fsql
from urllib.request import Request, urlopen


URL = 'fsql://test/fixtures/features.sql?date=2020-01-18&bob=uncle'
EXPECTATION = "SELECT * FROM features;\n"

REQ = Request(url=URL)
subject = fsql.FSQLHandler()


class TestGCSHandler:
    def test_gs_open(self):
        resp = subject.fsql_open(REQ)
        assert resp.read() == EXPECTATION

    def test_open(self):
        result = datasets.urlopen(URL)
        assert result.read() == EXPECTATION

    def test_urlopen(self):
        result = urlopen(URL)
        assert result.read() == EXPECTATION
