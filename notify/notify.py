#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from enum import Enum
from gi.repository import Notify
import os


IMG_DIR = 'ico'
MIC = 'mic.png'
LISTEN = 'listen.png'
WAIT = 'wait.png'

CUR_DUR = os.path.dirname(os.path.realpath(__file__))
LISTEN_ICON = os.path.join(CUR_DUR, IMG_DIR, LISTEN)
MIC_ICON = os.path.join(CUR_DUR, IMG_DIR, MIC)
WAIT_ICON = os.path.join(CUR_DUR, IMG_DIR, WAIT)


class NOTIFY_TYPE(Enum):
    LISTEN = 0
    MIC = 1
    WAIT = 2


notify_type_to_ico_map = {
    NOTIFY_TYPE.LISTEN: LISTEN_ICON,
    NOTIFY_TYPE.MIC: MIC_ICON,
    NOTIFY_TYPE.WAIT: WAIT_ICON,
}


class Notification(object):
    def __init__(self, app_name='USpeak'):
        self.app_name = app_name
        self.notify = None
        Notify.init(self.app_name)

    def show(self, message, notify_type=NOTIFY_TYPE.MIC):
        icon = notify_type_to_ico_map.get(notify_type)
        if self.notify:
            self.notify.props.body = message
            self.notify.props.icon_name = icon
        else:
            self.notify = Notify.Notification.new(self.app_name, message, icon)
        self.notify.show()


