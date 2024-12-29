from __future__ import with_statement
import contextlib

try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
import sys

def make_small(url):
    #   Append given url to TinyURL API address that creates a new link
    request_url = ('http://tinyurl.com/api-create.php?' + urlencode({'url':url}))
    with contextlib.closing(urlopen(request_url)) as response:
        print(response.read().decode('utf-8'))
        return response.read().decode('utf-8')

def main():
    #   Print out the shortened url.
    for smallUrl in map(make_small, sys.argv[1:]):
        print(smallUrl)
    
if __name__ == '__main__':
    main()