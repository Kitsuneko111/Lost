from view import View
from model import Model
import pygame


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.register(self)

    def getTile(self, index):
        return self.model.getTile(index)

    def move(self, direction):
        if not self.model.move or "freeplay" in self.model.activePowerups or "gravity" in self.model.activePowerups:
            self.model.move = direction

    def moveUpdate(self):
        self.model.moveGame()

    def getSpecials(self):
        return self.model.getSpecials()

    def press(self, num):
        powers = {pygame.K_1: "gravity", pygame.K_2: "anti-coins",
                  pygame.K_3: "freeplay", pygame.K_4: "clone", pygame.K_5: "combust"}
        self.model.activatePower(powers[num])

    def tick(self):
        self.model.clock += 1
        end = self.model.checks()
        if end:
            self.view.end()

    def restart(self):
        self.view = View()
        self.model = Model()
        self.view.register(self)
        self.view.startGame()

    def getTime(self):
        return str(self.model.clock//10)


if __name__ == "__main__":
    view = View()
    model = Model()
    #print(model.grid)
    controller = Controller(model, view)
    view.run()
