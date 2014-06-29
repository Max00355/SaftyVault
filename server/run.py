import socket
import json
import upload
import download
import get_dirs
import send_dirs
import thread
import get_names

class Server:
    def __init__(self):
        self.commands = {
                            "upload":upload.upload,
                            "download":download.download,
                            "get_dirs":get_dirs.get_dirs,
                            "send_dirs":send_dirs.send_dirs,
                            "get_names":get_names.get_names,
                        }   
    
        self.username = "root"
        self.password = "toor"
        self.port = 7777
        self.host = "0.0.0.0"

    def main(self):
        sock = socket.socket()
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((self.host, self.port))
        sock.listen(5)
        print "Safty Vault is running on port {}.".format(self.port)
        while True:
            obj, conn = sock.accept()
            thread.start_new_thread(self.handle, (obj,))
    
    def handle(self, obj):
        data = obj.recv(1024000000)
        print data
        data = json.loads(data)
        if data['username'] == self.username and data['password'] == self.password:
            if data['cmd'] in self.commands:
                self.commands[data['cmd']](obj, data)
        else:
            obj.close()


if __name__ == "__main__":
    Server().main()
    

