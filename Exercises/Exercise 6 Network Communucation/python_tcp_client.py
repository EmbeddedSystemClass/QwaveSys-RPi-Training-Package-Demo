#!/usr/bin/env python

"""
A simple echo client
"""

import sys
import socket

host = 'localhost'
port = 50001
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
count=0
data='Hello, LabVIEW!'


# Check the size of the data(in bytes) you're sending
#data_size = len(data);
#print >>sys.stderr, 'Data size:', data_size



# Send data string and read data from LabVIEW
while (count < 10):
   s.send('Hello, LabVIEW!')
   data = s.recv(size)
   print 'Received:', data
   count = count + 1
s.close()
