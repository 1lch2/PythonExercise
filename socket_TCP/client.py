from socket import *
import sys
import time

serverName = 'localhost'
serverPort = int(sys.argv[1])
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

file_name = sys.argv[2]

try:
    t_start = time.time()
    f0 = open(file_name, 'rb')
    data = f0.read()
    f0.close()
    clientSocket.send(data)

except IOError:
    print('No such file')

clientSocket.close()

# Command line prompt: py client.py portnumber filepath
