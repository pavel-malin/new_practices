# Event-driven inbound proccesing
import select
import socket


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Never blocks a thread on I/O
server.setblocking(0)

# Assigns a socket to a port
server.bind(('localhost', 10000))
server.listen(4)

while True:
    # select() returns 3 arrays containing an object(socket, files)
    # that are ready to be read, written, or couse an error.
    inputs, outputs, excepts = select.select([server], [], [server])
    if server in inputs:
        connection, client_address = server.accept()
        connection.send("hello!\n")
