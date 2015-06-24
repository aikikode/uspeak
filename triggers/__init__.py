#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import audioop
import time

import pyaudio


class LoudSoundTrigger:
    CHUNK = 1024
    THRESHOLD = 1000
    CHANNELS = 1
    RATE = 44100

    def __init__(self, callback, *args, chunk=CHUNK, threshold=THRESHOLD, **kwargs):
        self.callback = callback
        self.audio = pyaudio.PyAudio()
        self.chunk = chunk
        self.threshold = threshold
        self.args = args
        self.kwargs = kwargs

    def run_and_wait(self, single_run=True):
        stream = self.audio.open(
            format=pyaudio.paInt16, channels=self.CHANNELS, rate=self.RATE, input=True, frames_per_buffer=self.chunk
        )
        while True:
            rms = audioop.rms(stream.read(self.chunk), 2)
            if rms > self.threshold:
                stream.close()
                time.sleep(0.3)
                self.callback(*self.args, **self.kwargs)
                break
        if not single_run:
            time.sleep(0.3)
            self.run_and_wait(single_run)
