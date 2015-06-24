#!/usr/bin/env python3
# -*- coding: utf-8 -*-

try:
    from espeak import espeak

    def run(*args, **kwargs):
        text = ' '.join(map(str, args))
        espeak.synth(text)

except ImportError:
    def run(*args, **kwargs):
        pass
