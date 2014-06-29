import os
import base64

def download(obj, data):
    with open(data['data'], 'rb') as file:
        for x in file.readlines():
            obj.send(base64.b64encode(x))
    obj.close()
