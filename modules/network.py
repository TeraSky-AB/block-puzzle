import socket

class Network():
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.1.26"
        self.port = 5555
        self.addr = (self.server, self.port)

    def connect(self):
        try:
            self.client.connect(self.addr)
        except:
            print("Connection au serveur échoué")

    def send(self, data):
        try:
            self.client.send(data.encode("Utf-8"))
            return self.client.recv(4096)
        except socket.error as e:
            print(e)



