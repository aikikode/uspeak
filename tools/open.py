#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import subprocess


def run(*args, **kwargs):
    return subprocess.call('xdg-open {}'.format(args[0]), shell=True)
