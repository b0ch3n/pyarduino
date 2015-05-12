__author__ = 'Mateusz'
# -*- coding: utf-8 -*-

from server.arduino_connection import arduino
from server.connection.data_reporter_factory import get_pins_dictionary
from server.connection.data_reporter_factory import ArduinoReporterFactory
print("SERVER PART OF PYARDUINO PROJECT")
'''

ar1.open_connection()

ar2 = arduino.ArduinoConnection("SERIAL", "COM5")
ar2.open_connection()


ar1.close_connection()
'''
ar1 = arduino.ArduinoConnection("SERIAL", "COM5")
ar1.open_connection()
ardFact = ArduinoReporterFactory()
ardRep = ardFact.get_reporter()

for x in range(0, 10):
    ardRep.get_data_for_pins(get_pins_dictionary("ArduinoUnoTest"), ar1)
    ar1.board.pass_time(1)

ar1.close_connection()
