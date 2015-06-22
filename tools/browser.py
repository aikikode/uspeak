#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib.parse import urlparse
import webbrowser

DEFAULT_URL = 'https://google.com'


def run(*args):
    url = ' '.join(map(str, args))
    url = url or DEFAULT_URL
    if '.' not in url:
        url = '{}.com'.format(url)
    if not urlparse(url).scheme:
        url = 'http://{}'.format(url)
    webbrowser.open(url)
