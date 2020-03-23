import socket
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
        global STATE
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
        

class OutputThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        
    def run(self):
        global STATE
        print('waiting for data')
        while STATE:
            data = sock.recv(1024).decode()
            if data[:2] == 'inf':
                owner = data[3:]
                print('Owner is', owner)
            elif data[:2] == 'txt':
                print(owner + ':', data[3:])


SERV_IP = 'ff64.ddns.net'
SERV_PORT = 5000

nickname = input('Enter your nickname: ')
sock = socket.socket()
sock.connect((SERV_IP, SERV_PORT))
sock.send(('con' + nickname).encode())


it = InputThread()
ot = OutputThread()

it.start()
ot.start()