from socket import *
import time
import _thread

# Accept file from client.
def server(sock, addr, serverport):
    print('Receive connection from: ' + str(addr))
    fp = open(str(serverport), 'wb')
    while True:
        data = sock.recv(1024)
        if len(data) == 0:
            break
        fp.write(data)

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
