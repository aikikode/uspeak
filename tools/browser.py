#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib.parse import urlparse, quote
import webbrowser


def run(*args):
    url = ' '.join(map(str, args[0]))
    if '.' not in url:
        url = '{}.com'.format(url)
    url = quote(url, safe="/;%[]=:$())+,!?*@'~")
    if not urlparse(url).scheme:
        url = 'http://{}'.format(url)
    webbrowser.open(url)
