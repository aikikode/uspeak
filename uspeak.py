#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import speech_recognition as sr

from notify.notify import Notification, NOTIFY_TYPE


notify = Notification('USpeak')
r = sr.Recognizer(language='en')
with sr.Microphone() as source:
    notify.show('Waiting for voice command...', NOTIFY_TYPE.LISTEN)
    audio = r.listen(source)

try:
    notify.show('Processing...', NOTIFY_TYPE.WAIT)
    recognized_text = r.recognize(audio)
    notify.show(recognized_text)
except LookupError:
    notify.show('Could not understand audio', NOTIFY_TYPE.WAIT)
