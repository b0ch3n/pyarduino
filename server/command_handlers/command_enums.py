__author__ = 'B0CH3N'
# -*- coding: utf-8 -*-

from enum import Enum, unique
import re

@unique
class Commands(Enum):
    GET_ANALOG_VAL = "GET_ANALOG_VAL"
    GET_DIGITAL_VAL = "GET_DIGITAL_VAL"
    SET_DIGITAL_VAL = "SET_DIGITAL_VAL"

    def __str__(self):
        return self.value


def command_extractor(command):
    testRE = command.match("\$\$(.*)\$\$(.*)\$\$");
    print(testRE)

