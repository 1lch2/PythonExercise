from socket import *
import sys
import time
import json
import os
import struct

serverName = 'localhost'
serverPort = int(sys.argv[1])


def file_transfer(file_name):
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))

    # Build JSON message.    
    file_size = os.path.getsize(file_name)
    tcpmsg = {
        'filename': 'new_' + file_name,
        'filesize': file_size
    }
    head = json.dumps(tcpmsg)
    headsize = struct.pack('i', len(head))

    # Pack message head and head size, then send to server for later extraction.
    clientSocket.send(headsize)
    clientSocket.send(head.encode('utf-8'))

    # Send file to server.
    try:
        t_start = time.ctime()
        f0 = open(file_name, 'rb')
        data = f0.read()
        f0.close()
        clientSocket.send(data)
        print('File sent at:' + str(t_start))

    except IOError:
        print('No such file')

    clientSocket.close()

# Command line prompt: py client.py portnumber filepath
if __name__ == '__main__':
    file_name = sys.argv[2]
    file_transfer(file_name)
