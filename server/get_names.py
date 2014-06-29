import os
import json

def get_names(obj, data):
    names = []
    for directory, _, name in os.walk("files"):
        for name in name:
            names.append(directory+"/"+name)

    obj.send(json.dumps({"response":names}))
