__author__ = 'B0CH3N'
# -*- coding: utf-8 -*-

from enum import Enum, unique
import re

class InvalidCommandException(Exception):
    pass



@unique
class Commands(Enum):
    GET_ANALOG_VAL = "GET_ANALOG_VAL"
    GET_DIGITAL_VAL = "GET_DIGITAL_VAL"
    SET_DIGITAL_VAL = "SET_DIGITAL_VAL"

    def __str__(self):
        return self.value


def commands_extractor(command):
    commands_with_params = command.split("$$")
    del commands_with_params[-1:]
    del commands_with_params[0]
    com = []
    par = []
    for item in commands_with_params:
        com.append(re.match(r"(.*)\?\?(.*)", item).group(1))
        par.append(re.match(r"(.*)\?\?(.*)", item).group(2))

    com_params_dict = zip(com, par)
    com_params_dict = list(com_params_dict)

    print(com_params_dict)
    return com_params_dict

