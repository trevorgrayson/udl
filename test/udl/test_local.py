from pytest import mark
import datasets

# TODO
URL = 'file:///Users/trevorgrayson/projects/data-science/test/fixtures/README.md'
EXPECTATION = "# Fixtures for testing\n"


class TestGCSHandler:
    def test_open(self):
        result = datasets.urlopen(URL)
        assert result.read().decode("utf8") == EXPECTATION

    @mark.skip(reason="needs implementing")
    def test_relative(self):
        result = datasets.urlopen('test/fixtures/README.md')
        assert result.read().decode("utf8") == EXPECTATION
