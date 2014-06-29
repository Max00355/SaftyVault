import socket
import json
import utils

def get_dirs():
    data = {"cmd":"get_dirs", "username":utils.username, "password":utils.password}
    sock = socket.socket()
    sock.connect(utils.connect)
    sock.send(json.dumps(data))
    data = sock.recv(10240000)
    return json.loads(data)['response']
