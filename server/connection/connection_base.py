__author__ = 'CAD'
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
from server.connection.connection_enums import ConnectionStatus

class ConnectionBase(metaclass=ABCMeta, object):
    @abstractmethod
    def __init__(self):
        self._connectionType = "UNDEFINED"
        self._connectionStatus = ConnectionStatus.Closed
        self._portName = "UNDEFINED"
        self._board = None

    @abstractmethod
    def open_connection(self):
        return NotImplemented

    @abstractmethod
    def close_connection(self):
        return NotImplemented

    @property
    def connectionType(self):
        return self._connectionType

    @connectionType.setter
    def connectionType(self, value):
        self._connectionType = value

    @property
    def connectionStatus(self):
        return self._connectionStatus

    @connectionStatus.setter
    def connectionStatus(self, value):
        self._connectionStatus = value

    @property
    def portName(self):
        return self._portName

    @portName.setter
    def portName(self, value):
        self._portName = value

    @property
    def board(self):
        return self._board

    @portName.setter
    def board(self, value):
        self._board = value

