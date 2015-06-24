# -*- coding: utf-8 -*-

import audioop
import pyaudio


class LoudSoundTrigger:
    CHUNK = 4096
    THRESHOLD = 5000
    CHANNELS = 1
    RATE = 44100

    def __init__(self, callback, *args, chunk=CHUNK, threshold=THRESHOLD):
        self.callback = callback
        self.audio = pyaudio.PyAudio()
        self.chunk = chunk
        self.threshold = threshold
        self.args = args

    def run_and_wait(self, single_run=True):
        stream = self.audio.open(
            format=pyaudio.paInt16, channels=self.CHANNELS, rate=self.RATE, input=True, frames_per_buffer=self.chunk
        )
        while True:
            rms = audioop.rms(stream.read(self.chunk), 2)
            if rms > self.threshold:
                stream.close()
                self.callback(*self.args)
                break
        if not single_run:
            self.run_and_wait()
