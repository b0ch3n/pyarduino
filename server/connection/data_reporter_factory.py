__author__ = 'Mateusz'
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
import time
from helpers.CommandsHelper.commands_helpers import Commands

class DataReporterFactory(metaclass=ABCMeta):
    @abstractmethod
    def get_reporter(self):
        return NotImplemented

class ArduinoReporterFactory(DataReporterFactory):
    def get_reporter(self):
        return ArduinoReporter()


class Reporter(metaclass=ABCMeta):
    @abstractmethod
    def get_data_for_pins(self, com_par_dict, connection):
        return NotImplemented

class ArduinoReporter(Reporter):
    def get_data_for_pins(self, com_par_dict, connection):

        response = '$$'
        print("ArduinoReporter method...")
        print(com_par_dict)
        print("iterator:")
        for item in com_par_dict:
            print(item[0])
            if item[0] == Commands.GET_ANALOG_VAL.value:
                pin = int(item[1])
                connection.board.analog[pin].enable_reporting()
                val = None
                while val == None:
                   # time.sleep(0.5)
                    val = connection.board.analog[pin].read()
                    connection.board.analog[pin].disable_reporting()
                val = str(float(val)*5.0)
                val = val[:5]
                response = response + str(val) + "$$"
                print(response)


            elif item[0] == Commands.GET_DIGITAL_VAL.value:
                pin = int(item[1])
                connection.board.digital[pin].enable_reporting()
                val = 0
                val = connection.board.digital[pin].read()
                connection.board.digital[pin].disable_reporting()
                val = float(val)
                response = response + str(val) + "$$"
                print(response)
        return response


def get_pins_dictionary(board_type):
    if board_type == "ArduinoUno":
        return {
            'ANALOG': {'A0': 0, 'A1': 1, 'A2': 2, 'A3': 3, 'A4': 4, 'A5': 5},
            'DIGITAL': {'D0': 0, 'D1': 0, 'D2': 0, 'D3': 0, 'D4': 0, 'D5': 0,
                        'D6': 0, 'D7': 0, 'D8': 0, 'D9': 0, 'D10': 0, 'D11': 0, 'D12': 0, 'D13': 0}
            }
    elif board_type == "ArduinoUnoTest":
        return {
            'ANALOG': {'A0': 0}
            }