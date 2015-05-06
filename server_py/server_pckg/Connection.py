__author__ = 'CAD'
# -*- coding: utf-8 -*-
from connection_enums import ConnectionStatus
from abc import ABCMeta, abstractmethod

class Connection(metaclass=ABCMeta,object):
    @abstractmethod
    def __init__(self):
        self._connectionType = "UNDEFINED"
        self._connectionStatus = ConnectionStatus.Closed
        self._portName = "UNDEFINED"

    @property
    def name(self):
        return  self._connectionType
    @name.setter
    	def name(self, value):
    		self._connectionType = value


