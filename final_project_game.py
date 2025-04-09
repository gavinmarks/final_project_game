import pygame
import math

pygame.init()

width, height = 1000, 1000
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("super fun game")


#you got me fucked up if you think im putting all those coordinates in a list manually
tile_cords = []
tile_x_cords = []
tile_y_cords = []
count = 0

for i in range(10):
    tile_x_cords.append(count)
    tile_y_cords.append(count)
    count = count + 100

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
            pygame.draw.rect(screen, pygame.Color("white"), self.rect, 5)
        else:
            pygame.draw.rect(screen, pygame.Color("black"), self.rect, 5)

    def handle_click(self, pos):
        if self.rect.collidepoint(pos):
            self.selected = not self.selected
            return True
        return False


more_tiles = []
for x, y in tile_cords:
    tiles = Tile(x, y, 100, (pygame.Color("green")))
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