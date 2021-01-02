from random import *
import block


class Tile:
    def __init__(self, sides, middle=False):
        self.middle = middle
        if not sides:
            self.top = [True, False][randint(0, 1)]
            self.left = [True, False][randint(0, 1)]
            self.right = [True, False][randint(0, 1)]
            self.bottom = [True, False][randint(0, 1)]
        else:
            if "top" in sides:
                self.top = sides["top"]
            else:
                self.top = [True, False][randint(0, 1)]
            if "left" in sides:
                self.left = sides["left"]
            else:
                self.left = [True, False][randint(0, 1)]
            if "right" in sides:
                self.right = sides["right"]
            else:
                self.right = [True, False][randint(0, 1)]
            if "bottom" in sides:
                self.bottom = sides["bottom"]
            else:
                self.bottom = [True, False][randint(0, 1)]
        if not self.top and not self.left and not self.bottom and not self.right:
            self.top = True
        self.blocks = []
        self.generateSides(middle)

    def generateSides(self, middle):
        top = [block.Block(), block.Block() if not self.top else block.Air(), block.Block()]
        middle = [block.Air() if self.left else block.Block(), block.Player() if middle else block.randomTile(), block.Air() if self.right else block.Block()]
        bottom = [block.Block(), block.Air() if self.bottom else block.Block(), block.Block()]
        self.blocks = [top, middle, bottom]

    def printVal(self):
        rows = []
        for row in self.blocks:
            string = ""
            for tile in row:
                string += tile.type
            rows.append(string)
        return rows

    def updateToMiddle(self):
        self.blocks[1][1] = block.Player()

    def updateFromMiddle(self):
        if self.blocks[1][1].type == "X":
            self.blocks[1][1] = block.Air()

    def hasSpecial(self):
        return self.blocks[1][1].type == "P" or self.blocks[1][1].type == "C"

    def addSpecial(self):
        if self.blocks[1][1].type == "P":
            return "P", self.blocks[1][1].powerup
        elif self.blocks[1][1].type == "C":
            return "C", self.blocks[1][1].size

    def duplicate(self):
        blocks = []
        for row in self.blocks:
            newRow = []
            for tile in row:
                newRow.append(tile.duplicate())
            blocks.append(newRow)
        return blocks


class Grid:
    def __init__(self, tiles=None):
        if not tiles:
            self.tiles = []
            self.generateInitialGrid()
        else:
            self.tiles = tiles

    def generateNewTile(self, sides=None, middle=False):
        return Tile(sides, middle)

    def generateNewSide(self, side):
        if side == "top":
            tops = [self.tiles[0][0].top, self.tiles[0][1].top, self.tiles[0][2].top]
            #print(tops)
            if tops[1]:
                middle = self.generateNewTile({"bottom": True})
            else:
                middle = self.generateNewTile({"bottom": False})
            left = self.generateNewTile({"right": middle.left, "bottom": tops[0]})
            right = self.generateNewTile({"left": middle.right, "bottom": tops[2]})
            return [left, middle, right]
        elif side == "left":
            lefts = [self.tiles[0][0].left, self.tiles[1][0].left, self.tiles[2][0].left]
            if lefts[1]:
                middle = self.generateNewTile({"right": True})
            else:
                middle = self.generateNewTile({"right": False})
            top = self.generateNewTile({"bottom": middle.top, "right": lefts[0]})
            bottom = self.generateNewTile({"top": middle.bottom, "right": lefts[2]})
            return [top, middle, bottom]
        elif side == "right":
            rights = [self.tiles[0][2].right, self.tiles[1][2].right, self.tiles[2][2].right]
            if rights[1]:
                middle = self.generateNewTile({"left": True})
            else:
                middle = self.generateNewTile({"left": False})
            top = self.generateNewTile({"bottom": middle.top, "left": rights[0]})
            bottom = self.generateNewTile({"top": middle.bottom, "left": rights[2]})
            return [top, middle, bottom]
        elif side == "bottom":
            bottoms = [self.tiles[2][0].bottom, self.tiles[2][1].bottom, self.tiles[2][2].bottom]
            if bottoms[1]:
                middle = self.generateNewTile({"top": True})
            else:
                middle = self.generateNewTile({"top": False})
            left = self.generateNewTile({"right": middle.left, "top": bottoms[0]})
            right = self.generateNewTile({"left": middle.right, "top": bottoms[2]})
            return [left, middle, right]

    def generateNewSideInit(self, side):
        if side == "top":
            tops = [self.tiles[1][0].top, self.tiles[1][1].top, self.tiles[1][2].top]
            #print(tops)
            if tops[1]:
                middle = self.generateNewTile({"bottom": True})
            else:
                middle = self.generateNewTile({"bottom": False})
            left = self.generateNewTile({"right": middle.left, "bottom": tops[0]})
            right = self.generateNewTile({"left": middle.right, "bottom": tops[2]})
            return [left, middle, right]
        elif side == "left":
            lefts = [self.tiles[0][1].left, self.tiles[1][1].left, self.tiles[2][1].left]
            if lefts[1]:
                middle = self.generateNewTile({"right": True})
            else:
                middle = self.generateNewTile({"right": False})
            top = self.generateNewTile({"bottom": middle.top, "right": lefts[0]})
            bottom = self.generateNewTile({"top": middle.bottom, "right": lefts[2]})
            return [top, middle, bottom]
        elif side == "right":
            rights = [self.tiles[0][1].right, self.tiles[1][1].right, self.tiles[2][1].right]
            if rights[1]:
                middle = self.generateNewTile({"left": True})
            else:
                middle = self.generateNewTile({"left": False})
            top = self.generateNewTile({"bottom": middle.top, "left": rights[0]})
            bottom = self.generateNewTile({"top": middle.bottom, "left": rights[2]})
            return [top, middle, bottom]
        elif side == "bottom":
            bottoms = [self.tiles[1][0].bottom, self.tiles[1][1].bottom, self.tiles[1][2].bottom]
            if bottoms[1]:
                middle = self.generateNewTile({"top": True})
            else:
                middle = self.generateNewTile({"top": False})
            left = self.generateNewTile({"right": middle.left, "top": bottoms[0]})
            right = self.generateNewTile({"left": middle.right, "top": bottoms[2]})
            return [left, middle, right]

    def generateInitialGrid(self):
        middle = self.generateNewTile(middle=True)
        left = self.generateNewTile({"right": middle.left})
        right = self.generateNewTile({"left": middle.right})
        self.tiles = [[], [left, middle, right], []]
        top = self.generateNewSideInit("top")
        bottom = self.generateNewSideInit("bottom")
        self.tiles = [top, [left, middle, right], bottom]

    def updateMiddle(self):
        self.tiles[1][1].updateToMiddle()
        self.tiles[0][1].updateFromMiddle()
        self.tiles[2][1].updateFromMiddle()
        self.tiles[1][0].updateFromMiddle()
        self.tiles[1][2].updateFromMiddle()

    def duplicate(self):
        tiles = []
        for row in self.tiles:
            newRow = []
            for tile in row:
                newRow.append(Tile({"top": tile.top, "left":tile.left, "right":tile.right, "bottom":tile.left}, tile.middle))
            tiles.append(newRow)
        return Grid(tiles)

    def __str__(self):
        rows = []
        for row in self.tiles:
            lines = ["", "", ""]
            for i in range(3):
                for tile in row:
                    lines[i] += tile.printVal()[i]
            rows.append("\n".join(lines))
        return "\n".join(rows)


class Model:
    def __init__(self):
        self.grid = Grid()
        #print(self.grid.tiles)
        self.move = None
        self.coins = 200
        self.powerups = {}
        self.activePowerups = {}
        self.clock = 0
        self.active = -1
        self.clones = []
        self.moveTicks = 1

    def clone(self, looseMoney = True):
        clone = {"grid": self.grid.duplicate(), "coins": self.coins//2 if looseMoney else self.coins}
        self.clones.append(clone)
        if looseMoney:
            self.coins //= 2

    def combust(self):
        self.coins = 0
        if len(self.clones):
            self.active = 0
            newGame = self.clones.pop()
            self.grid = newGame["grid"]
            self.coins = newGame["coins"]
            #self.activePowerups.pop("clone")
            self.powerups["clone"] = 0
        self.powerups["combust"] = 0

    def checks(self):
        #print(self.clock)
        popPowers = []
        for power in self.activePowerups:
            if power == "clone":
                if len(self.clones) == 0:
                    popPowers.append("clone")
                    self.powerups[power] = 0
            if self.activePowerups[power] == self.clock:
                popPowers.append(power)
                self.powerups[power] = 0
                if power == "freeplay":
                    self.moveTicks = 1
        for power in popPowers:
            self.activePowerups.pop(power)
            #print(self.activePowerups)
        noCoins = False
        if self.coins == 0:
            noCoins = True
            for cloneDict in self.clones:
                if cloneDict["coins"] != 0:
                    noCoins = False
        return noCoins

    def activatePower(self, power):
        if power == "combust":
            if power in self.powerups:
                if self.powerups[power] == 1:
                    self.combust()
                    return
        if power == "clone":
            if power in self.powerups:
                if self.powerups[power] == 1:
                    self.clone()
                    self.powerups[power] = 2
                    return
                elif self.powerups[power] == 2:
                    self.active = self.active + 1 % len(self.clones)
                    self.clone(looseMoney=False)
                    newDict = self.clones.pop(self.active-1)
                    self.grid = newDict["grid"]
                    self.coins = newDict["coins"]
        if power == "freeplay":
            if power in self.powerups:
                if self.powerups[power] == 1:
                    self.moveTicks = 2
        if power == "gravity":
            if "freeplay" in self.activePowerups:
                return
        if power == "freeplay":
            if "gravity" in self.activePowerups:
                return
        if power in self.powerups:
            if self.powerups[power] == 1:
                self.powerups[power] = 2
                self.activePowerups[power] = self.clock+300

    def getSpecials(self):
        specials = {}
        for power in self.powerups:
            specials[power] = self.powerups[power]
        specials["coins"] = self.coins
        return specials

    def getTile(self, index):
        return self.grid.tiles[index[1]][index[0]]

    def moveGame(self):
        execs = {"up": self.up,
                 "left": self.left,
                 "right": self.right,
                 "down": self.down}

        if "gravity" in self.activePowerups:
           if not self.move and self.grid.tiles[1][1].bottom:
                self.move = "down"
        #print(self.move, self.clock % self.moveTicks)
        if "freeplay" in self.activePowerups and self.move:
            execs[self.move]()
            self.move = None

        elif self.move:
            execs[self.move]()
        self.grid.updateMiddle()

    def up(self):
        if self.grid.tiles[1][1].top:
            if self.grid.tiles[0][1].hasSpecial():
                specialType, special = self.grid.tiles[0][1].addSpecial()
                #print(specialType)
                if specialType == "C":
                    #print("coin")
                    if "anti-coins" not in self.activePowerups:
                        self.coins += special
                    else:
                        self.coins -= special
                else:
                    if special not in self.powerups:
                        self.powerups[special] = 1
                    elif self.powerups[special] == 0:
                        self.powerups[special] = 1
            side = self.grid.generateNewSide("top")
            self.grid.tiles.pop(2)
            self.grid.tiles.insert(0, side)
        else:
            self.move = None

    def left(self):
        if self.grid.tiles[1][1].left:
            if self.grid.tiles[1][0].hasSpecial():
                specialType, special = self.grid.tiles[1][0].addSpecial()
                #print(specialType)
                if specialType == "C":
                    #print("coin")
                    if "anti-coins" not in self.activePowerups:
                        self.coins += special
                    else:
                        self.coins -= special
                else:
                    if special not in self.powerups:
                        self.powerups[special] = 1
                    elif self.powerups[special] == 0:
                        self.powerups[special] = 1
            side = self.grid.generateNewSide("left")
            for i in range(3):
                self.grid.tiles[i].pop(2)
                self.grid.tiles[i].insert(0, side[i])
        else:
            self.move = None

    def down(self):
        if self.grid.tiles[1][1].bottom:
            if self.grid.tiles[2][1].hasSpecial():
                specialType, special = self.grid.tiles[2][1].addSpecial()
                #print(specialType)
                if specialType == "C":
                    #print("coin")
                    if "anti-coins" not in self.activePowerups:
                        self.coins += special
                    else:
                        self.coins -= special
                else:
                    if special not in self.powerups:
                        self.powerups[special] = 1
                    elif self.powerups[special] == 0:
                        self.powerups[special] = 1
            side = self.grid.generateNewSide("bottom")
            self.grid.tiles.pop(0)
            self.grid.tiles.append(side)
        else:
            self.move = None

    def right(self):
        if self.grid.tiles[1][1].right:
            if self.grid.tiles[1][2].hasSpecial():
                specialType, special = self.grid.tiles[1][2].addSpecial()
                #print(specialType)
                if specialType == "C":
                    #print("coin")
                    if "anti-coins" not in self.activePowerups:
                        self.coins += special
                    else:
                        self.coins -= special
                else:
                    if special not in self.powerups:
                        self.powerups[special] = 1
                    elif self.powerups[special] == 0:
                        self.powerups[special] = 1
            side = self.grid.generateNewSide("right")
            for i in range(3):
                self.grid.tiles[i].pop(0)
                self.grid.tiles[i].append(side[i])
        else:
            self.move = None
