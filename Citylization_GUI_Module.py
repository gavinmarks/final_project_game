import pygame

pygame.init()

scale = 100
width, height = 600, 600
screen = pygame.display.set_mode((width, height))

class button:
    def __init__(self, x, y, SizeX, SizeY, text):
        self.x = x
        self.y = y
        self.SizeX = SizeX
        self.SizeY = SizeY
        self.name = 'button'
        self.scale = scale
        self.text = text
        self.rect = pygame.Rect(self.x, self.y, self.SizeX, self.scale)

    def draw(self, frame):
        pygame.draw.rect(screen, "red", self.rect)
        print(self.x, self.y, self.scale)

class clickMenu:
    def __init__(self, x, y, scale, options):
        self.x = x
        self.y = y
        self.name = 'popupMenu'
        self.scale = scale
        self.rect = pygame.Rect(self.x, self.y, self.scale*2, self.scale*4)
        
    def close(self):
        del self
        
    def draw(self, screen):
        pygame.draw.rect(screen, "white", self.rect)
        print(self.x, self.y, self.scale)

    

    



popMenu = 0
running = True
while running:
    print(popMenu)
    screen.fill("black")
    if popMenu != 0:
        popMenu.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                if popMenu != 0:
                    popMenu.close()
                print('rightClickDetected')
                menuX, menuY = event.pos
                print(menuX, menuY)
                popMenu = clickMenu(menuX, menuY, scale, 'A')
                popMenu.draw(screen)
                print('rightClickActionDone')

    pygame.display.update()

pygame.quit()
