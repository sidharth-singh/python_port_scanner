#!/usr/bin/python

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = ""

for port in range(49000):
    reply = s.connect_ex((host, port))
    if reply == 0:
        print "Port no. : " + str(port) + " is open"
    else:
        continue
