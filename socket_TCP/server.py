from socket import *
import time
import _thread
import json
import struct


buffersize = 1024

# Accept file from client.
def server(sock, addr, serverport):
    # Receive head info.
    head_len_num = sock.recv(4) # Receive the nuumber of the size for the head segment.
    if head_len_num:
        print('Receive connection from: ' + str(addr))

    headsize = struct.unpack('i', head_len_num)[0] # Get the size of the head segment.
    headdata = sock.recv(headsize) # Receive head segment.

    # Extract the head message,
    head_decode = json.loads(headdata.decode('utf-8'))
    filename = head_decode['filename']
    filesize = head_decode['filesize']

    # Receive file from client.
    recvsize = 0
    fp = open(filename, 'wb')
    while recvsize < filesize:
        if filesize - recvsize > buffersize:
            recvdata = sock.recv(buffersize)
            fp.write(recvdata)
            recvsize += len(recvdata)
        else:
            recvdata = sock.recv(filesize - recvsize)
            recvsize += len(recvdata)
            fp.write(recvdata)

    print('File received size:' + str(recvsize))
    print('File received name:' + filename)

    fp.close()
    sock.close()
    print('Connection closed.')

# Start multi-thread TCP server socket.
def start():
    servername = '127.0.0.1'
    serverport = 10086

    print('Server start at port: ' + str(serverport))
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind((servername, serverport))
    serverSocket.listen()

    while(True):
        print('Waiting for connection...')
        s, addr = serverSocket.accept()
        _thread.start_new_thread(server, (s, addr, serverport))

    serverSocket.close()

if __name__ =='__main__':
    start()
