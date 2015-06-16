#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import importlib

from dictionary.logic import read_dictionary, translate
import speech_recognition as sr

from notify.notify import Notification, NOTIFY_TYPE


def main():
    notify = Notification('USpeak')
    dictionary = read_dictionary()
    r = sr.Recognizer(language='en')
    with sr.Microphone() as source:
        notify.show('Waiting for voice command...', NOTIFY_TYPE.LISTEN)
        audio = r.listen(source)
    notify.show('Processing...', NOTIFY_TYPE.WAIT)
    try:
        recognized_text = r.recognize(audio)
    except LookupError:
        notify.show('Could not understand audio', NOTIFY_TYPE.WAIT)
        return
    notify.show(recognized_text)

    command = translate(recognized_text, dictionary=dictionary)
    cmd = command.split()[0]
    cmd_module = importlib.import_module('tools.{}'.format(cmd))
    cmd_module.run(command.split()[1:])


if __name__ == '__main__':
    main()
