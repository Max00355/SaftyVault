import socket
import utils
import json
import base64

def download(filename):
    data = json.dumps({"cmd":"download", "data":filename, "username":utils.username, "password":utils.password})
    sock = socket.socket()
    sock.connect(utils.connect)
    sock.send(data)
    with open(filename, 'wb') as file:
        while True:
            data = sock.recv(1024)
            if data:
                file.write(base64.b64decode(data))
            else:
                break

    sock.close()
