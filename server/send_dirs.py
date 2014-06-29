import os

def send_dirs(obj, data):
    for x in data['data']:
        if not os.path.exists(x):
            os.mkdir(x)

    obj.close()
