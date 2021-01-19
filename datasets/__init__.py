from urllib.request import urlopen, build_opener, install_opener
from .gcs import GCSHandler
from .fsql import FSQLHandler

HANDLERS = [
    GCSHandler(),
    FSQLHandler(),
]
install_opener(build_opener(*[handler for handler in HANDLERS]))
