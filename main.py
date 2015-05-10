__author__ = 'Mateusz'


from server.arduino_connection import arduino

print("SERVER PART OF PYARDUINO PROJECT")

ar1 = arduino.ArduinoConnection("USB", "COM5")
ar2 = arduino.ArduinoConnection("SERIAL", "COM2")
ar1.open_connection()

