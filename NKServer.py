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
            sock.send('txt' + input('>').encode())
        

class OutputThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        
    def run(self):
        print('waiting data')
        while True:
            data=sock.recv(1024).decode()
            if data[:2] == 'con':
                conector=data[3:]
                print(conector, 'connected')
                sock.send('inf' + nickname.encode())
            elif data[:2] == 'dcn':
                print(conector,'disconnected')
                conector=''
            elif data[:2] == 'txt':
                print(conector + '>',data[3:])

nickname = input('Enter your nickname: ')

sock = socket.socket()
sock.bind(('ff64.ddns.net', 5000))
sock.listen(5)
conn, addr = sock.accept()

it = InputThread()
ot = OutputThread()

it.start()
ot.start()