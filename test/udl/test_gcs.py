import datasets
from urllib.request import Request, urlopen

URL = 'gs://davesci/test.md'
EXPECTATION = "# test file\n"

REQ = Request(url=URL)
subject = datasets.gcs.GCSHandler()


class TestGCSHandler:
    def test_gs_open(self):
        resp = subject.gs_open(REQ)
        assert resp.read().decode("utf8") == EXPECTATION

    def test_open(self):
        result = datasets.urlopen(URL)
        assert result.read().decode("utf8") == EXPECTATION

    def test_urlopen(self):
        result = urlopen(URL)
        assert result.read().decode("utf8") == EXPECTATION
