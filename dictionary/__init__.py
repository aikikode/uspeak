#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re

TEXT_PATTERN = 'text'
CUR_DUR = os.path.dirname(os.path.realpath(__file__))
DATA_DIR = os.path.join(CUR_DUR, 'data')


def get_dictionary_file_by_lang(language):
    return os.path.join(DATA_DIR, 'main_{}.dic'.format(language))


def read_dictionary(dictionary_file=None, language='en'):
    regex_map = []
    if not dictionary_file and language:
        dictionary_file = get_dictionary_file_by_lang(language)
    try:
        with open(dictionary_file) as dictionary_f:
            regex = None
            for line in dictionary_f:
                line = line.rstrip('\n')
                if line.startswith('#'):
                    continue
                is_regex = not line.startswith(' ')
                line = line.strip(' ')
                if is_regex:
                    regex = re.compile(line, re.IGNORECASE)
                elif regex is not None:
                    regex_map.append((regex, line, ))
    except FileNotFoundError:
        return []
    return regex_map


def translate(message, dictionary=None):
    if not dictionary:
        dictionary = read_dictionary()
    text_sub = re.compile('\<{}\>'.format(TEXT_PATTERN), re.IGNORECASE)
    for regex, command in dictionary:
        match = regex.search(message)
        if match:
            try:
                return text_sub.sub(match.group(TEXT_PATTERN), command)
            except IndexError:
                return command
