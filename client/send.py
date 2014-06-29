import socket
import utils

def send(data):
    s = socket.socket()
    s.connect(utils.connect)
    s.send(data)
    s.close()
