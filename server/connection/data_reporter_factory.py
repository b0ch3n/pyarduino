__author__ = 'Mateusz'
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class DataReporterFactory(metaclass=ABCMeta):
    @abstractmethod
    def get_reporter(self):
        return NotImplemented

class ArduinoReporterFactory(DataReporterFactory):
    def get_reporter(self):
        return ArduinoReporter()


class Reporter(metaclass=ABCMeta):
    @abstractmethod
    def get_data_for_pins(self, dict, connection):
        return NotImplemented

class ArduinoReporter(Reporter):
    def get_data_for_pins(self, dict , connection):
        for key, value in dict["ANALOG"].items():
            connection.board.analog[value].enable_reporting()
        for i in range(1, 11):
            for key, value in dict["ANALOG"].items():
                print("Pin %s-%i : %s" % (key, value, connection.board.analog[value].read()))
                connection.board.pass_time(1)


def get_pins_dictionary(board_type):
    if board_type == "ArduinoUno":
        return {
            'ANALOG': {'A0': 0, 'A1': 1, 'A2': 2, 'A3': 3, 'A4': 4, 'A5': 5},
            'DIGITAL': {'D0': 0, 'D1': 0, 'D2': 0, 'D3': 0, 'D4': 0, 'D5': 0,
                        'D6': 0, 'D7': 0, 'D8': 0, 'D9': 0, 'D10': 0, 'D11': 0, 'D12': 0, 'D13': 0}
            }
