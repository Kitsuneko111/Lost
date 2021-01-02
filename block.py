from random import randint


class Block:
    def __init__(self):
        self.type = "B"
        self.colour = "#ffffff"

    def duplicate(self):
        return Block()

    def __str__(self):
        return "B"


class Air:
    def __init__(self):
        self.type = " "
        self.colour = "#000000"

    def duplicate(self):
        return Air()

    def __str__(self):
        return " "


class PowerUp:
    def __init__(self, powerUp=None, colour=None):
        self.type = "P"
        if not powerUp:
            randomVal = randint(0, 16)
            self.colour = ["#0000ff", "#777722", "#00ff00", "#aa0000", "#0000ff", "#777722", "#00ff00", "#aa0000", "#0000ff", "#777722", "#00ff00", "#aa0000", "#0000ff", "#777722", "#00ff00", "#aa0000", "#aaaaaa"][randomVal]
            self.powerup = ["gravity", "anti-coins", "freeplay", "clone", "gravity", "anti-coins", "freeplay", "clone", "gravity", "anti-coins", "freeplay", "clone", "gravity", "anti-coins", "freeplay", "clone", "combust"][randomVal]
        else:
            self.colour = colour
            self.powerup = powerUp

    def duplicate(self):
        return PowerUp(self.powerup, self.colour)

    def __str__(self):
        return "P"


class Coin:
    def __init__(self, size=None):
        self.type = "C"
        self.colour = "#ffff00"
        if not size:
            self.size = randint(1, 10)
        else:
            self.size = size

    def duplicate(self):
        return Coin(self.size)

    def __str__(self):
        return "C"


class Player:
    def __init__(self):
        self.type="X"
        self.colour = "#ff0000"

    def duplicate(self):
        return Player()


def randomTile():
    tileType = randint(0, 6)
    if tileType == 1:
        return PowerUp()
    elif tileType == 2:
        return Coin()
    else:
        return Air()
