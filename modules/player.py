class Player():
    def __init__(self):
        self.points = 0
        self.draw = []
        self.bonuses = []

    def addPoints(self, nb):
        self.points += nb
