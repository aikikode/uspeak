#!/usr/bin/env python3
# -*- coding: utf-8 -*-

try:
    from espeak import espeak
except ImportError:
    class espeak():
        @classmethod
        def synth(*args):
            pass


def run(*args, **kwargs):
    text = ' '.join(map(str, args))
    espeak.synth(text)
