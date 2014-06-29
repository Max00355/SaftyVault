import os
import time
import thread
import send_dirs
import get_dirs
import get_names
import download
import upload

class Client:
    def __init__(self):
        self.files = {}
        self.dirs = []

    def main(self):
    
        print "Safty Vault is running."
        while True:
            if self.check_directories():
                send_dirs.send_dirs(self.dirs)
            
            check = self.check_files()
            if check:
                for x in check:
                    upload.upload(x)

            for x in get_dirs.get_dirs():
                if not os.path.exists(x):
                    os.mkdir(x)

            for x in get_names.get_names():
                if not os.path.exists(x):
                    download.download(x)

            print self.files
            time.sleep(1)

    def check_directories(self):
        new = False
        for directory,_,_ in os.walk("files"):
            if directory not in self.dirs:
                self.dirs.append(directory)
                new = True
        print new
        return new


    def check_files(self):
        new = []
        for directory, _, files in os.walk("files"):
           for files in files:
                if directory+"/"+files not in self.files:
                    self.files[directory+"/"+files] = hash(open(directory+"/"+files, 'rb').read())
                    new.append(directory+"/"+files)
                elif hash(open(directory+"/"+files, 'rb').read()) != self.files[directory+"/"+files]:
                    self.files[directory+"/"+files] = hash(open(directory+"/"+files, 'rb').read())
                    new.append(directory+"/"+files)
        print new
        return new
    

if __name__ == "__main__":
    Client().main()
