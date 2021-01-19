# UDL: Uniform Data Locator

URL "Protocol" plugins for Python3.

This project started off as a router that would let you open up many URL types,
regardless of protocol.  It turns out that core python has a rad, extensible, 
library: [urllib.request](https://docs.python.org/3.9/library/urllib.request.html).

It deals with "mostly HTTP."  This library is meant to extend it.

## Usage

```python3

import udl  # registers additional handlers.

f = udl.urlopen('gs://your_bucket/your/filename.md')
f.read()  # standard python file object interface

```


## Supported Protocols

- HTTP, HTTPS, FTP - Stock `urllib.requests.urlopen`
- GS - Google Cloud Storage
