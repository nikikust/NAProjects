#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

sock = socket.socket()
sock.connect(('ff64.ddns.net', 5000))
print('connected')
data = sock.recv(1024)
sock.close()

print(data)
print('done')
while 1:
    continue
