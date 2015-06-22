#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import importlib

import speech_recognition as sr

from dictionary.logic import read_dictionary, translate
from notify import Notification, NOTIFY_TYPE, NOTIFY_LEVEL
from tools import media


def uspeak(lang):
    notify = Notification('USpeak')
    dictionary = read_dictionary()
    r = sr.Recognizer(language=lang)
    with sr.Microphone() as source:
        # Mute all sounds not to interfere with user input
        # Check if muted
        if not media.is_muted():
            media.volume('mute')
            turn_on_sounds = True
        else:
            turn_on_sounds = False
        notify.show('Waiting for voice command...', NOTIFY_TYPE.LISTEN, NOTIFY_LEVEL.CRITICAL)
        try:
            audio = r.listen(source, timeout=3)
        except TimeoutError:
            notify.hide()
            return
        finally:
            if turn_on_sounds:
                media.volume('unmute')
    notify.show('Processing...', NOTIFY_TYPE.WAIT, NOTIFY_LEVEL.CRITICAL)
    try:
        recognized_text = r.recognize(audio)
    except LookupError:
        notify.show('Could not understand audio', notify_type=NOTIFY_TYPE.WAIT)
        return

    command = translate(recognized_text, dictionary=dictionary)
    if command:
        notify.show(recognized_text)
        cmd = command.split()[0]
        cmd_module = importlib.import_module('tools.{}'.format(cmd))
        if cmd_module.run(*command.split()[1:]):
            notify.show('Sorry, there were some problems running your command.', notify_type=NOTIFY_TYPE.WAIT)
    else:
        notify.show('Unknown command: {}'.format(recognized_text))


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='USpeak.')
    parser.add_argument('--lang', type=str, default='en', help='language to use for commands (default: en)')
    args = parser.parse_args()
    uspeak(args.lang)
