import pygame


class View:
    def __init__(self):
        pygame.init()
        self.size = 500
        self.tickClock = pygame.time.Clock()
        self.win = pygame.display.set_mode((self.size, self.size+75))
        self.c = None
        self.blockWidth = self.size // 9
        self.runGame = True
        pygame.display.set_caption("LOST!")
        img = pygame.image.load("./lost.PNG")
        pygame.display.set_icon(img)

    def register(self, c):
        self.c = c

    def drawEnd(self):
        pygame.draw.rect(self.win, "#ffffff", (0, 0, self.size, self.size+75))
        font = pygame.font.Font("Early GameBoy.ttf", 60)
        render = font.render("YOU WIN!", True, "#000000")
        size = render.get_size()
        self.win.blit(render, (self.size//2-size[0]//2, self.size//2-size[1]//2))
        font = pygame.font.Font("Early GameBoy.ttf", 18)
        render = font.render("Press SPACE to play again!", True, "#000000")
        size = render.get_size()
        self.win.blit(render, (self.size//2-size[0]//2, self.size//2-size[1]//2+40))
        font = pygame.font.Font("Early GameBoy.ttf", 24)
        render = font.render("You took "+self.c.getTime()+"s.", True, "#000000")
        size = render.get_size()
        self.win.blit(render, (self.size//2-size[0]//2, self.size//2-size[1]//2+100))
        pygame.display.update()

    def end(self):
        ended = True
        while ended:
            self.drawEnd()
            self.tickClock.tick(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    ended = False
                    self.runGame = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.c.restart()
                        ended = False

    def run(self):
        running = True
        while running:
            self.drawStart()
            self.tickClock.tick(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
                    self.runGame = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        running = False
                        self.startGame()

    def drawStart(self):
        pygame.draw.rect(self.win, "#666666", (0, 0, self.size, self.size+75))
        font = pygame.font.Font("Early GameBoy.ttf", 70)
        render = font.render("LOST!", True, "#ffffff")
        size = render.get_size()
        self.win.blit(render, (self.size//2-size[0]//2, self.size//2-size[1]//2))
        font = pygame.font.Font("Early GameBoy.ttf", 18)
        render = font.render("Press SPACE to START!", True, "#ffffff")
        size = render.get_size()
        self.win.blit(render, (self.size//2-size[0]//2, self.size//2-size[1]//2+40))
        font = pygame.font.Font("Early GameBoy.ttf", 14)
        render = font.render("Once you move you won't stop.", True, "#ffffff")
        size = render.get_size()
        self.win.blit(render, (self.size // 2 - size[0] // 2, self.size // 2 - size[1] // 2+60))

        img = pygame.image.load("./gravity/2.png")
        self.win.blit(img, (self.size//6-img.get_size()[0]//2, self.size//2-img.get_size()[1]//2-110))
        font = pygame.font.Font("Early GameBoy.ttf", 12)
        render = font.render("Enable gravity", True, "#0000ff")
        size = render.get_size()
        self.win.blit(render, (self.size // 6 - size[0] // 2, self.size // 2 - size[1] // 2-110-75-10))

        img = pygame.image.load("./anti-coins/2.png")
        self.win.blit(img, ((self.size // 6)*3 - img.get_size()[0] // 2, self.size // 2 - img.get_size()[1] // 2 - 110- 75 - 10))
        font = pygame.font.Font("Early GameBoy.ttf", 12)
        render = font.render("Coins are negative", True, "#777722")
        size = render.get_size()
        self.win.blit(render, ((self.size // 6)*3 - size[0] // 2, self.size // 2 - size[1] // 2 - 110 ))

        img = pygame.image.load("./freeplay/2.png")
        self.win.blit(img,
                      ((self.size // 6) * 5 - img.get_size()[0] // 2, self.size // 2 - img.get_size()[1] // 2 - 110))
        font = pygame.font.Font("Early GameBoy.ttf", 12)
        render = font.render("Move anywhere", True, "#00ff00")
        size = render.get_size()
        self.win.blit(render, ((self.size // 6) * 5 - size[0] // 2, self.size // 2 - size[1] // 2 - 110 - 75 - 10))

        img = pygame.image.load("./clone/2.png")
        self.win.blit(img,
                      ((self.size // 6) * 1 - img.get_size()[0] // 2, self.size // 2 - img.get_size()[1] // 2 + 70 + 75 + 20 + 20))
        font = pygame.font.Font("Early GameBoy.ttf", 12)
        render = font.render("Clone a new you", True, "#aa0000")
        size = render.get_size()
        self.win.blit(render, ((self.size // 6) * 1 - size[0] // 2, self.size // 2 - size[1] // 2 + 70 + 75 + 10 + 75 + 10 + 20))

        img = pygame.image.load("./combust/2.png")
        self.win.blit(img,
                      ((self.size // 6) * 3 - img.get_size()[0] // 2,
                       self.size // 2 - img.get_size()[1] // 2 + 70 + 75 + 10 + 10 + 20))
        font = pygame.font.Font("Early GameBoy.ttf", 12)
        render = font.render("Explode and loose your coins", True, "#aaaaaa")
        size = render.get_size()
        self.win.blit(render, ((self.size // 6) * 3 - size[0] // 2, self.size // 2 - size[1] // 2 + 70 + 10 + 20))

        img = pygame.image.load("./coin/0.png")
        self.win.blit(img,
                      ((self.size // 6) * 5 - img.get_size()[0] // 2,
                       self.size // 2 - img.get_size()[1] // 2 + 70 + 75 + 20 + 20))
        font = pygame.font.Font("Early GameBoy.ttf", 12)
        render = font.render("The Evil", True, "#ffff00")
        size = render.get_size()
        self.win.blit(render, ((self.size // 6) * 5 - size[0] // 2, self.size // 2 - size[1] // 2 + 70 + 75 + 10 + 75 + 10 + 20))
        pygame.display.update()

    def startGame(self):
        while self.runGame:
            self.tickClock.tick(10)
            self.drawGame()
            self.c.tick()
            if self.runGame:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        self.runGame = False
                        break
            if self.runGame:
                keys = pygame.key.get_pressed()
                nums = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5]
                for number in nums:
                    if keys[number]:
                        self.c.press(number)
                if keys[pygame.K_DOWN]:
                    self.c.move("down")
                if keys[pygame.K_UP]:
                    self.c.move("up")
                if keys[pygame.K_LEFT]:
                    self.c.move("left")
                if keys[pygame.K_RIGHT]:
                    self.c.move("right")
                self.c.moveUpdate()

    def drawGame(self):
        pygame.draw.rect(self.win, "#666666", (0, 0, self.size, self.size+75))
        for i in range(9):
            self.drawTile((i % 3, i // 3))
        specials = self.c.getSpecials()
        specialVals = ["gravity", "anti-coins", "freeplay", "clone", "combust"]
        for i in range(5):
            if specialVals[i] in specials:
                img = pygame.image.load("./"+specialVals[i]+"/"+str(specials[specialVals[i]])+".png")
            else:
                img = pygame.image.load("./"+specialVals[i]+"/0.png")
            self.win.blit(img, (75*i, self.size))
        img = pygame.image.load("./coin/0.png")
        self.win.blit(img, (5*75, self.size))
        font = pygame.font.Font("Early GameBoy.ttf", 22)
        render = font.render(str(specials["coins"]), True, (0, 0, 0))
        size = render.get_size()
        self.win.blit(render, (int(5.5*75-size[0]//2), self.size + 75 // 2 - size[1]//2))
        pygame.display.update()

    def drawTile(self, index):
        tile = self.c.getTile(index)
        for i in range(9):
            pygame.draw.rect(self.win, tile.blocks[i // 3][i % 3].colour,
                             (index[0]*self.blockWidth*3+(i % 3)*self.blockWidth,
                              index[1]*self.blockWidth*3+(i // 3)*self.blockWidth,
                              self.blockWidth,
                              self.blockWidth))
