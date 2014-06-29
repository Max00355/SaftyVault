import send
import json
import utils

def send_dirs(dirs):
    data = json.dumps({"cmd":"send_dirs", "data":dirs, "username":utils.username, "password":utils.password})
    send.send(data)
