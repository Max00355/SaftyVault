import socket
import utils
import json

def get_names():
    sock = socket.socket()
    sock.connect(utils.connect)
    sock.send(json.dumps({"username":utils.username, "password":utils.password, "cmd":"get_names"}))
    data = sock.recv(1024000)
    return json.loads(data)['response']

