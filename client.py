import socket
from threading import Thread


class InputThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        
    def run(self):
        while True:
            s.send(input().encode())
        

class OutputThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        
    def run(self):
        while True:
            print(s.recv(1024).decode())


SERV_IP = 'ff64.ddns.net'
SERV_PORT = 5000

nickname = input('Enter your nickname: ')
s = socket.socket()
s.connect((SERV_IP, SERV_PORT))
s.send(nickname.encode() + ' has connected!')


it = InputThread()
ot = OutputThread()

it.start()
ot.start()