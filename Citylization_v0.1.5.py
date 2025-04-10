import pygame
import math

pygame.init()

xSize = 15
ySize = 40
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("CivLike v0.1.5")

#fits map into largest area possible that still fits the window
def scaleAdjust(scaleBy):
    print("width: ", width, "| height: ", height)
    returnScale = min(width, height)/scaleBy
    print("the scale is:", returnScale)
    return returnScale

scale = scaleAdjust(max(xSize, ySize))


#you got me fucked up if you think im putting all those coordinates in a list manually
tile_cords = []

#makes list for all (x, y) pairs
for i1 in range(xSize):
    for i2 in range(ySize):
        tile_cords.append((i1, i2))
        
print(tile_cords)

class Tile:
    def __init__(self, x, y, size, color,):
        self.x = x*size
        self.y = y*size
        self.name = (x, y)
        self.size = size
        self.color = color
        self.selected = False
        self.rect = pygame.Rect(self.x, self.y, size, size)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        if self.selected:
            pygame.draw.rect(screen, pygame.Color("white"), self.rect, round((2*self.size)/scale))
        else:
            pygame.draw.rect(screen, pygame.Color("black"), self.rect, round((2*self.size)/scale))

    def handle_click(self, pos):
        if self.rect.collidepoint(pos):
            self.selected = not self.selected
            return True
        return False


#list contains coordinates and tile instances for each coordinate. *NEEDS TO BE FIXED SO THAT COORDINATE WORK AS ADDRESSES FOR INSTANCES
#btw list looks like eldritch abomination, might need debugging for duplicates
more_tiles = []
for x, y in tile_cords:
    tiles = Tile(x, y, scale, (pygame.Color("green")))
    more_tiles.append((tiles.name, tiles))

print(more_tiles)



running = True

while running:
    screen.fill(pygame.Color("white")) 


    for name, tile in more_tiles:
        tile.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for tile in more_tiles:
                tile.selected = False
            for tile in more_tiles:
                if tile.handle_click(pos):
                    print(f"Tile at ({tile.x}, {tile.y}) was clicked")
                    break
        elif event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
