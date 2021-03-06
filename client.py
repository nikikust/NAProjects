import socket
import sys
from threading import Thread

global owner
global STATE

STATE = 1
owner = ''
data = ''

'''
class Mail(object):
    def __init__(self):
        pass

    def send(text,cmd = ''):
        if cmd == '':
'''

class InputThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        
    def run(self):
        global STATE, owner
        sock.send(('con' + nickname).encode())
        while STATE:
            mail = input('>')
            cmd = []
            if mail[0] == '/':
                cmd = mail[1:].split(' ')
                if cmd[0] == 'leave':
                    sock.send('dcn'.encode())
                    STATE = 0
                else:
                    print('Invalid command')
            else:
                sock.send(('txt' + mail).encode())
        sys.exit()
        

class OutputThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        
    def run(self):
        global STATE, owner
        print('waiting for data')
        while STATE:
            data = sock.recv(1024).decode()
            if data[:3] == 'inf':
                owner = data[3:]
                print('Owner is', owner)
            elif data[:3] == 'txt':
                print(owner + ':', data[3:])
        sys.exit()

SERV_IP = 'ff64.ddns.net'
SERV_PORT = 5000

nickname = input('Enter your nickname: ')
sock = socket.socket()
sock.connect((SERV_IP, SERV_PORT))

it = InputThread()
ot = OutputThread()

it.start()
ot.start()