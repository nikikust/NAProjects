import socket
import sys
from threading import Thread
import time

data=''
conector=''

class InputThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        
    def run(self):
        while True:
            conn.send(('txt' + input('>')).encode())
        

class OutputThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        
    def run(self):
        print('waiting data')
        while True:
            data=conn.recv(1024).decode()
            if data[:3] == 'con':
                conector=data[3:]
                print(conector, 'connected')
                conn.send(('inf' + nickname).encode())
            elif data[:3] == 'dcn':
                print(conector,'disconnected')
                conector=''
            elif data[:3] == 'txt':
                print(conector + '>',data[3:])

nickname = input('Enter your nickname: ')

sock = socket.socket()
sock.bind(('ff64.ddns.net', 30000))
sock.listen(5)

print('started')

conn, addr = sock.accept()

it = InputThread()
ot = OutputThread()

it.start()
ot.start()