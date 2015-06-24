#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib.parse import urlparse
import webbrowser

from pygoogle import PyGoogle

DEFAULT_URL = 'https://google.com'


def run(*args, **kwargs):
    lang = kwargs.get('lang', 'en')
    url = ' '.join(map(str, args))
    url = url or DEFAULT_URL
    if '.' not in url:
        # Try to find corresponding site
        pygoogle = PyGoogle(url, pages=1, hl=lang)
        url = pygoogle.get_urls()[0]
    if not urlparse(url).scheme:
        url = 'http://{}'.format(url)
    webbrowser.open(url)
