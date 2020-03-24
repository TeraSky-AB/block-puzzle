import pickle
import socket
import threading


class threadedClient(threading.Thread):  # Si le joueur join, il doit envoyer son adresse en premier
    def __init__(self, conn, p, gameID ):
        threading.Thread.__init__(self)
        self.conn = conn
        self.player = p
        self.gameID = gameID

    def run(self):
        while True:
            data = self.conn.recv(2048).decode()
            if gameID in games:
                if not data:
                    break
                else:
                    if data == "go":
                        games[self.gameID]["state"] = "gameover"
                        print("Game", self.gameID, "is over")
                        self.conn.send(pickle.dumps(games[self.gameID]["playersPoints"]))
                    elif data == "get-points":
                        self.conn.send(pickle.dumps(games[self.gameID]["playersPoints"]))
                        print("Player", self.player, "from game", self.gameID,"requested point state")
                    elif data[0:11] == "set-points:":
                        games[gameID]["playersPoints"][self.player] = int(data[11:])
                        print("Player", self.player, "from game", self.gameID, "set his points to", data[11:])
                        self.conn.send("1".encode())
                    elif data == "get-state":
                        self.conn.send(games[self.gameID]["state"].encode())
            else:
                conn.send("return".encode())


server = "192.168.1.26"
port = 5555

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sock.bind((server, port))
except socket.error as err:
    print(err)

sock.listen()
print("Server started, now waiting connection..")

connectedPersons = set()
games = {}
idCount = 0

while True:
    conn, addr = sock.accept()
    print(addr[0], "connected")

    idCount += 1
    p = 0
    gameID = (idCount-1)//2
    if idCount % 2 == 1:
        games[gameID] = {
            "playersPoints": [0, 0],
            "state": "waiting",
        }
        newThread = threadedClient(conn, 0, gameID)
    else:
        games[gameID]["state"] = "running"
        newThread = threadedClient(conn, 1, gameID)
    newThread.start()
