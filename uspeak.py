#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import importlib

from dictionary import read_dictionary, translate, show_commands
from notify import Notification, NOTIFY_TYPE, NOTIFY_LEVEL
import speech_recognition as sr
from tools import say
from tools.media import reduced_volume
from triggers import LoudSoundTrigger


def run_command(command, lang):
    cmd = command.split()[0]
    module_name = 'tools.{}'.format(cmd)
    try:
        cmd_module = importlib.import_module(module_name)
    except ImportError:
        print('ERROR: module {} not found'.format(module_name))
        return 1
    return cmd_module.run(*command.split()[1:], lang=lang)


def uspeak(lang, use_sounds):
    notify = Notification('USpeak')
    r = sr.Recognizer(language=lang)
    with sr.Microphone() as source:
        with reduced_volume():
            if use_sounds:
                say.run('go')
            notify.show('Waiting for voice command...', NOTIFY_TYPE.OK, NOTIFY_LEVEL.CRITICAL)
            try:
                audio = r.listen(source, timeout=3)
            except TimeoutError:
                notify.show('Sorry, could not hear your voice', notify_type=NOTIFY_TYPE.ERROR)
                return
    notify.show('Working on it...', NOTIFY_TYPE.MIC, NOTIFY_LEVEL.CRITICAL)
    try:
        recognized_text = r.recognize(audio)
    except LookupError:
        notify.show('Could not understand your phrase, try again please', notify_type=NOTIFY_TYPE.ERROR)
        return

    command = translate(recognized_text, dictionary=read_dictionary(language=lang))
    if command:
        notify.show('Executing: {}.\nReady for another command.'.format(command), notify_type=NOTIFY_TYPE.OK)
        if run_command(command, lang):
            notify.show('Sorry, there were some problems running your command.', notify_type=NOTIFY_TYPE.ERROR)
    else:
        notify.show('Unknown command: {}'.format(recognized_text), notify_type=NOTIFY_TYPE.ERROR)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='USpeak: control PC with your voice')
    parser.add_argument('--lang', '-l', type=str, default='en', help='language that you speak (default: en)')
    parser.add_argument(
        '--sounds', '-s', action='store_true',
        help='use computer voice that tells you when the program is ready to listen to your commands'
    )
    parser.add_argument(
        '--continuous', '-c', action='store_true',
        help='run continuously waiting for voice input triggered by loud sound'
    )
    parser.add_argument('--list-commands', action='store_true', help='List available voice commands')
    parser.add_argument(
        '--trigger', '-t', type=str,
        help='ADVANCED: provide command to execute if sound level exceeds the limit. See available commands format in'
             ' dict files: dictionary/data/*.dic'
    )
    args = parser.parse_args()
    if args.list_commands:
        show_commands(args.lang)
    elif args.trigger:
        LoudSoundTrigger(run_command, args.trigger, args.lang).run_and_wait(single_run=not args.continuous)
    elif args.continuous:
        LoudSoundTrigger(uspeak, args.lang, args.sounds).run_and_wait(single_run=False)
    else:
        uspeak(args.lang, args.sounds)
