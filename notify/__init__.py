#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from enum import Enum
from gi.repository import Notify
import os


IMG_DIR = 'ico'
MIC = 'mic.png'
OK = 'ok.png'
ERROR = 'error.png'

CUR_DUR = os.path.dirname(os.path.realpath(__file__))
OK_ICON = os.path.join(CUR_DUR, IMG_DIR, OK)
MIC_ICON = os.path.join(CUR_DUR, IMG_DIR, MIC)
ERROR_ICON = os.path.join(CUR_DUR, IMG_DIR, ERROR)


class NOTIFY_TYPE(Enum):
    OK = 0
    MIC = 1
    ERROR = 2


class NOTIFY_LEVEL():
    LOW = Notify.Urgency.LOW
    NORMAL = Notify.Urgency.NORMAL
    CRITICAL = Notify.Urgency.CRITICAL


notify_type_to_ico_map = {
    NOTIFY_TYPE.OK: OK_ICON,
    NOTIFY_TYPE.MIC: MIC_ICON,
    NOTIFY_TYPE.ERROR: ERROR_ICON,
}


class Notification(object):
    def __init__(self, app_name='USpeak'):
        self.app_name = app_name
        self.notify = None
        Notify.init(self.app_name)

    def show(
        self, message, notify_type=NOTIFY_TYPE.MIC, notify_level=NOTIFY_LEVEL.NORMAL, timeout=4000
    ):
        icon = notify_type_to_ico_map.get(notify_type)
        if self.notify:
            self.notify.props.body = message
            self.notify.props.icon_name = icon
        else:
            self.notify = Notify.Notification.new(self.app_name, message, icon)
        self.notify.set_urgency(notify_level)
        if timeout and notify_level != NOTIFY_LEVEL.CRITICAL:
            self.notify.set_timeout(timeout)
        self.notify.show()

    def hide(self):
        if self.notify:
            self.notify.close()


