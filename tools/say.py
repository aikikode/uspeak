#!/usr/bin/env python3
# -*- coding: utf-8 -*-

try:
    from espeak import espeak
except ImportError:
    class espeak():
        @classmethod
        def synth(*args):
            print('Cannot generate speech. Please, install python3-espeak module.')
            return 1


def run(*args, **kwargs):
    text = ' '.join(map(str, args))
    espeak.synth(text)
