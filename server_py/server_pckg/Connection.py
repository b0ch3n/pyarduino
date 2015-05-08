__author__ = 'CAD'
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
from server_py.server_pckg.connection_enums import ConnectionStatus


class Connection(metaclass=ABCMeta, object):
    @abstractmethod
    def __init__(self):
        self._connectionType = "UNDEFINED"
        self._connectionStatus = ConnectionStatus.Closed
        self._portName = "UNDEFINED"

    @property
    def name(self):
        return self._connectionType

    @name.setter
    def name(self, value):
        self._connectionType = value

    @property
    def name(self):
        return self._connectionType

    @name.setter
    def name(self, value):
        self._connectionType = value

        @property
    def name(self):
        return self._connectionType

    @name.setter
    def name(self, value):
        self._connectionType = value
