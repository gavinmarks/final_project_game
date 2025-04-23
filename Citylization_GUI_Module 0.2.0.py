import pygame
import math

pygame.init()
pygame.font.init()


scale = 100
width, height = 1200, 800
screen = pygame.display.set_mode((width, height))

renderListP = []
renderListS = []


my_font = pygame.font.SysFont('Cambria', 30) 


def isDivisible(a, b):
    if b == 0:
        return false
    return a%b == 0

class Frame:
    def __init__(self, xPos, yPos, xSize, ySize):
        self.xPos = xPos
        self.yPos = yPos
        self.ySize = xSize
        self.ySize = ySize
        self.Color = "grey"
        self.rect = pygame.Rect(self.xPos, self.yPos, self.xSize, self.ySize)

    def draw(self, screen):
        pygame.draw.rect(screen, self.Color, self.rect)
        
    def close(self):
        del self

class button:
    def __init__(self, x, y, SizeX, SizeY, Frame, text):
        self.x = x
        self.y = y
        self.SizeX = SizeX
        self.SizeY = SizeY
        self.name = 'button'
        self.scale = scale
        self.text = text
        self.rect = pygame.Rect(self.x - self.SizeX/2, self.y - self.SizeY/2, self.SizeX, self.SizeY)
        self.frame = Frame
        self.text_surface = my_font.render(text, True, 'black')

    def draw(self, screen):
        pygame.draw.rect(screen, "grey", self.rect)
        screen.blit(self.text_surface,(self.text_surface.get_rect( center = (self.rect.center))))
        
    def close(self):
        del self

class clickMenu:
    def __init__(self, x, y, scale, options):
        self.x = x
        self.y = y
        self.name = 'clickMenu'
        self.scale = scale
        self.rect = pygame.Rect(self.x, self.y, self.scale*2, (self.scale*(2/3))*len(options))
        self.options = options
        self.buttons = []
        
        var = 0
        print('vartest', len(options)/2)
        if isDivisible(len(options)/2, 1):
            var = -(len(options)/2)+0.5
        else:
            var = -math.floor(len(options)/2)
        
        for option in options:
            print(var)
            adjustY = (var*self.rect.height/len(options))
            adjustX = self.scale
            buttonkey = button(self.rect.center[0], self.rect.center[1]+adjustY, self.scale*1.5, self.rect.height/(len(options)+1), self.rect, option)
            buttonkey.draw(screen)
            print(buttonkey)
            self.buttons.append(buttonkey)
            var += 1
            
        
        
    def close(self):
        for buttonkey in self.buttons:
            buttonkey.close
        renderListP.remove(popMenu)
        print("delete check")
        del self
        
    def draw(self, screen):
        pygame.draw.rect(screen, "white", self.rect)
        for button in self.buttons:
            button.draw(screen)

  

    



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
            if popMenu != 0:
                    print("popmenu", popMenu)
                    popMenu.close()
                    print("remove check")
                    popMenu = 0
            if event.button == 3:
                print('rightClickDetected')
                menuX, menuY = event.pos
                print(menuX, menuY)
                popMenu = clickMenu(menuX, menuY, scale, ['OptionA', 'OptionB', 'OptionC', 'OptionD', 'OptionE'])
                print("check:", popMenu)
                popMenu.draw(screen)
                renderListP.append(popMenu)
                print('rightClickActionDone')
            else:
                if popMenu != 0:
                    popMenu.close

    pygame.display.update()

pygame.quit()
