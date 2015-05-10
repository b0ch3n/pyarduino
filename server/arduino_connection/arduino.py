__author__ = 'Mateusz'

from ..connection.connection_base import ConnectionBase
from ..connection.connection_enums import ConnectionStatus
from pyfirmata import Arduino, util

class ArduinoConnection(ConnectionBase):
    def __init__(self, connection_type, port_name):
        super().__init__()
        self.connectionStatus = ConnectionStatus.Closed
        self.connectionType = connection_type
        self.portName = port_name

    def open_connection(self):
        self.board = Arduino(self.portName)
        print("Opened connection for {}, {} , on port: ".format(self.connectionType, self.board, self.portName))

    def close_connection(self):
        return NotImplemented







