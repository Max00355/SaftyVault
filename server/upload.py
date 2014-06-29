import os
import base64

def upload(obj, data):
    first = True
    file_name = data['name']
    with open(file_name, 'wb') as file:
        file.write(base64.b64decode(data['data']))
    obj.close()
