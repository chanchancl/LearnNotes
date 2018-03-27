
import socket
import selectors
import time

Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

Socket.bind(('127.0.0.1', 8000))
print('Binding socket at : 127.0.0.1:8000')

Socket.listen(5)
print('Start Listening...')

_exit = False

with selectors.SelectSelector() as selector:
    selector.register(Socket, selectors.EVENT_READ)

    while not _exit:
        ready = selector.select(0.5)

        if ready:
            request, client_address = Socket.accept()
            data = request.recv(1024).decode('utf-8')
            print(data)
            request.send(('[%s]Received : %s' % (time.ctime(),data)).encode())



