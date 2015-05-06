__author__ = 'CAD'
# -*- coding: utf-8 -*-

from enum import Enum, unique

@unique
class ConnectionStatus(Enum):
    Closed = "Connection closed!"
    Open = "Connection open!"
    Busy = "Connection busy!"

    def __str__(self):
        return self.value



