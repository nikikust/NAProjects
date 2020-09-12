import socket
import sys
from threading import Thread
import time

global data, connector, conn, addr, STATE

connector = ''
STATE = 1

class InputThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        
    def run(self):
        global STATE
        while STATE:
            conn.send(('txt' + input('>')).encode())
        

class OutputThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        
    def run(self):
        global conn, addr, STATE
        data = ''
        print('waiting data')
        while STATE:
            data=conn.recv(1024).decode()
            if data[:3] == 'con':
                connector = data[3:]
                print(connector, 'connected')
                conn.send(('inf' + nickname).encode())
            elif data[:3] == 'dcn':
                print(connector, 'disconnected')
                connector = ''
                STATE = 0
                #conn, addr = sock.accept()
            elif data[:3] == 'txt':
                print(connector + '>', data[3:])

nickname = input('Enter your nickname: ')

sock = socket.socket()
sock.bind(('ff64.ddns.net', 5000))
sock.listen(5)

print('started')

conn, addr = sock.accept()

it = InputThread()
ot = OutputThread()

it.start()
ot.start()