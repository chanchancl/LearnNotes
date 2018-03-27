
import socket
import time

i = 1
while True:
    try:
        Socket = socket.create_connection(('127.0.0.1',8000))
    except Exception as e:
        print(e)
    Socket.send(('%s'%i).encode())
    i = i+1
    data = Socket.recv(1024).decode('utf-8')
    print( data )
    time.sleep(0.01)
    Socket.close()
