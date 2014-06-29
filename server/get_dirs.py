import os
import json

def get_dirs(obj, data):
    out = {"response":[]}
    for directory,_,_ in os.walk("files"):
        out['response'].append(directory)

    obj.send(json.dumps(out))
    obj.close()
