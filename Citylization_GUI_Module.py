import pygame

pygame.init()

scale = 100
width, height = 600, 600
screen = pygame.display.set_mode((width, height))

renderListP = []
renderListS = []

class button:
    def __init__(self, x, y, SizeX, SizeY, Frame, text):
        self.x = x
        self.y = y
        self.SizeX = SizeX
        self.SizeY = SizeY
        self.name = 'button'
        self.scale = scale
        self.text = text
        self.rect = pygame.Rect(self.x, self.y, self.SizeX, self.scale)
        self.frame = Frame

    def draw(self, screen):
        pygame.draw.rect(screen, "black", self.rect)
        
    def close(self):
        del self

class clickMenu:
    def __init__(self, x, y, scale, options):
        self.x = x
        self.y = y
        self.name = 'popupMenu'
        self.scale = scale
        self.rect = pygame.Rect(self.x, self.y, self.scale*2, self.scale*4)
        self.options = options
        self.buttons = []
        for option in options:
            adjustY = self.y + scale
            buttonkey = button(self.x, self.y + adjustY, self.scale*1.5, self.scale, self.rect, option)
            buttonkey.draw(screen)
            print(buttonkey)
            renderListS.append(buttonkey)
            self.buttons.append(buttonkey)
            
        
        
    def close(self):
        for buttonkey in self.buttons:
            buttonkey.close
            renderList.remove(buttonkey)
        print("delete check")
        del self
        
    def draw(self, screen):
        pygame.draw.rect(screen, "white", self.rect)

    

    



popMenu = 0
running = True
while running:
    screen.fill("black")
    for item in renderListP:
        item.draw(screen)
        
    for item in renderListS:
        item.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                if popMenu != 0:
                    print("popmenu", popMenu)
                    popMenu.close
                    renderListP.remove(popMenu)
                    print("remove check")
                print('rightClickDetected')
                menuX, menuY = event.pos
                print(menuX, menuY)
                popMenu = clickMenu(menuX, menuY, scale, 'A')
                print("check:", popMenu)
                popMenu.draw(screen)
                renderListP.append(popMenu)
                print('rightClickActionDone')
            else:
                if popMenu != 0:
                    popMenu.close

    pygame.display.update()

pygame.quit()
