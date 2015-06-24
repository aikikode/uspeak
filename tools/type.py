#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from gi.repository import Gtk
from gi.repository import Gdk
import subprocess


def run(*args, **kwargs):
    text = ' '.join(map(str, args))
    cb = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
    cb.set_text(text, -1)
    cb.store()
    subprocess.call("xte 'keydown Shift_R' 'key Insert' 'keyup Shift_R'", shell=True)

