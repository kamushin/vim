#!/usr/bin/python
import os

try:
    from bs4 import BeautifulSoup
except ImportError:
    pass

class foo(object):
    def __init__(self):
        super(foo, self).__init__()
    
class bar(foo):
    pass


