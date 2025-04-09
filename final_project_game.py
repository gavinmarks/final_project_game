import pygame
import math

pygame.init()

gridSize= 10
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("CivLike v0.1.2")

def scaleAdjust(tiles):
    print("width: ", width, "| height: ", height)
    returnScale = min(width, height)/tiles
    print("the scale is:", returnScale)
    return returnScale

scale = scaleAdjust(gridSize)


#you got me fucked up if you think im putting all those coordinates in a list manually
tile_cords = []
tile_x_cords = []
tile_y_cords = []
count = 0

for i in range(gridSize):
    tile_x_cords.append(count)
    tile_y_cords.append(count)
    count = count + 1

for i1 in tile_x_cords:
    for i2 in tile_y_cords:
        tile_cords.append((i1, i2))


class Tile:
    def __init__(self, x, y, size, color,):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.selected = False
        self.rect = pygame.Rect(x, y, size, size)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        if self.selected:
            pygame.draw.rect(screen, pygame.Color("white"), self.rect, gridSize/2)
        else:
            pygame.draw.rect(screen, pygame.Color("black"), self.rect, gridSize/2)

    def handle_click(self, pos):
        if self.rect.collidepoint(pos):
            self.selected = not self.selected
            return True
        return False


more_tiles = []
for x, y in tile_cords:
    tiles = Tile(x*scale, y*scale, scale, (pygame.Color("green")))
    more_tiles.append(tiles)


running = True

while running:
    screen.fill(pygame.Color("white")) 


    for tile in more_tiles:
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
