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
import threading

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

def clientThread(conn, lock):
    user_id = uuid.uuid4()
    while user_id in connected_clients:
        user_id =uuid.uuid4()
    connected_clients.append(user_id)
    print("Uruchomiono wątek dla klienta o id: " + str(user_id))
    while True:
        try:
            data = conn.recv(32)
            if not data:
                break
            print("Odebrana komenda od klienta o id:" + str(user_id) + " : " + data.decode())
            with lock:
                try:
                    voltage = str(ardRep.get_data_for_pins(get_pins_dictionary("ArduinoUnoTest"), ar1))
                    print('Wysylam:')
                    print(voltage)
                    conn.sendall(voltage.encode())
                except:
                    conn.sendall("ERROR".encode())
        except ConnectionResetError:
            print("Polaczenie zerwane...")
            break
    print("Zamykanie polaczenia z klientem o id: " + str(user_id))
    connected_clients.remove(user_id)
    conn.close()



s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 8888))
s.listen(5)
lock = threading.Lock()

while 1:
    print("Awaiting for client...")
    client, addr = s.accept()
    print("Polaczenie z {}".format(addr))
    cThread = threading.Thread(target=clientThread, args=(client, lock))
    cThread.start()


client.close()
ar1.close_connection()
