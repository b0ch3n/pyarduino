__author__ = 'Mateusz'
# -*- coding: utf-8 -*-

from server.arduino_connection import arduino
from server.connection.data_reporter_factory import get_pins_dictionary
from server.connection.data_reporter_factory import ArduinoReporterFactory
from socket import *
from _thread import *
from time import *
import struct
import binascii
import uuid

print("SERVER PART OF PYARDUINO PROJECT")

connected_clients = []
try:
    ar1 = arduino.ArduinoConnection("SERIAL", "COM5")
    ar1.open_connection()
    ardFact = ArduinoReporterFactory()
    ardRep = ardFact.get_reporter()
except:
    print("Some error occurred...")
    raise SystemExit

def clientThread(conn):
    while True:
        user_id = uuid.uuid4()
        while user_id in connected_clients:
            user_id =uuid.uuid4()
        connected_clients.append(user_id)
        data = conn.recv(1024)
        print("Uruchomiono wątek dla klienta o id: " + user_id)
        if not data:
            break
        print(data)
        reply = 'chuj'
        conn.sendall(reply.encode())
    connected_clients.remove(user_id)
    conn.close()



s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 8888))
s.listen(5)

while 1:
    print("Awaiting for client...")
    client, addr = s.accept()
    print("Polaczenie z {}".format(addr))
    start_new_thread(clientThread, (client,))
    #volt = ardRep.get_data_for_pins(get_pins_dictionary("ArduinoUnoTest"), ar1)
    #v = str(volt)
    #print(v)
    #client.send(v.encode()) # wyslanie danych do klienta
client.close()



'''
for x in range(0, 10):
    ardRep.get_data_for_pins(get_pins_dictionary("ArduinoUnoTest"), ar1)
    ar1.board.pass_time(1)
'''
ar1.close_connection()
