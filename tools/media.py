#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess


def volume(delta, *args):
    if delta:
        return subprocess.call('amixer -D pulse set Master 1+ {}'.format(delta), shell=True)
    return 1


command_to_method = {
    'volume': volume,
    'next': lambda *args: subprocess.call("xte 'keydown XF86AudioNext' 'keyup XF86AudioNext'", shell=True),
    'prev': lambda *args: subprocess.call("xte 'keydown XF86AudioPrev' 'keyup XF86AudioPrev'", shell=True),
    'pause': lambda *args: subprocess.call("xte 'keydown XF86AudioPlay' 'keyup XF86AudioPlay'", shell=True),
}


def run(*args):
    try:
        media_action = command_to_method.get(args[0])
        return media_action(*args[1:])
    except IndexError:
        return 1
