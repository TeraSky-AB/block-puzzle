import socket

class Network():
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, scoket.SOCK_STREAM)
        self.server = "192.168.1.26"
        self.port = 5000
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def connect(self):
        try:
            self.client.connect(self.addr)
        except:
            pass

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)
