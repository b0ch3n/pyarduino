__author__ = 'Mateusz'
# -*- coding: utf-8 -*-

from ..connection.connection_base import ConnectionBase
from ..connection.connection_enums import ConnectionStatus
from pyfirmata import Arduino, util
import serial

class ArduinoConnection(ConnectionBase):
    def __init__(self, connection_type, port_name):
        super().__init__()
        self.connectionStatus = ConnectionStatus.Closed
        self.connectionType = connection_type
        self.portName = port_name
        self._iterator = None

    def open_connection(self):
        if self.connectionStatus == ConnectionStatus.Open:
            print(self.connectionStatus)
            return None
        try:
            if self.board is None:
                print("Initializing board object specified connected to port {} ...".format(self.portName))
                self.board = Arduino(self.portName)
                print("Board object created!")
            if self._iterator is None:
                print("Initializing iterator object to prevent overflow serial buffer ...")
                self._iterator = util.Iterator(self.board)
                print("Iterator object created!")
                self._iterator.start()
            self.connectionStatus = ConnectionStatus.Open
            print("{}, {} , {} ".format(self.connectionStatus, self.connectionType, self.portName))

        except serial.SerialException as e:
            print(e.args[0])
            if self.board is not None:
                self.board.exit()
            raise SystemExit

    def close_connection(self):
        if self.connectionStatus == ConnectionStatus.Closed:
            print("Connection is already closed!")
        else:
            self.board.exit()
            self.board = None
            self._iterator = None
            self.connectionStatus = ConnectionStatus.Closed
            print(self.connectionStatus)












