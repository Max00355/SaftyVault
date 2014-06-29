import socket
import utils
import json
import base64

def upload(x):
    sock = socket.socket()
    sock.connect(utils.connect)

    with open(x, 'rb') as file:
        sock.send(json.dumps({"cmd":"upload", "data":base64.b64encode(file.read()), "name":x, "username":utils.username, "password":utils.password}))

    sock.close()
