import pygame
import math

pygame.init()

x_size = 15
y_size = 15
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("CivLike v0.1.5")

#toggle to True for debug print statments so the terminal doesnt fill every time
DEBUG = True

#fits map into largest area possible that still fits the window
def scaleAdjust(scaleBy):
    print("width: ", width, "| height: ", height)
    returnScale = min(width, height)/scaleBy
    print("the scale is:", returnScale)
    return returnScale

scale = scaleAdjust(max(x_size,y_size))

# makes a list of all x, y coordinates
tile_coords = []

for i in range(y_size):
    row = []
    for j in range(x_size):
        row.append((j,i))
    tile_coords.append(row)

if DEBUG:
    print(f"tile_coords are", tile_coords)

class Tile:
    def __init__(self, x, y, size, color, scale):
        self.x = x * size
        self.y = y * size
        self.name = (x, y)
        self.size = size
        self.color = color
        self.scale = scale
        self.selected = False
        self.rect = pygame.Rect(self.x, self.y, size, size)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        border_color = pygame.Color("white") if self.selected else pygame.Color("black")
        pygame.draw.rect(screen, border_color, self.rect, round((2 * self.size) / self.scale))

    def handle_click(self, pos):
        if self.rect.collidepoint(pos):
            self.selected = not self.selected
            return True
        return False
    
class Player:
    def __init__(self, x, y, name, size, color, scale):
        self.x = x * size
        self.y = y * size
        self.name = name
        self.size = size
        self.color = color
        self.scale = scale
        self.rect = pygame.Rect(self.x, self.y, size, size)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

#dictionary for tile coordinates
tile_map = {}
for row in tile_coords:
    for x, y in row:
        tile = Tile(x, y, scale, pygame.Color("green"), scale)
        tile_map[(x, y)] = tile

if DEBUG:
    print(tile_map)

running = True
player = None
while running:
    screen.fill(pygame.Color("white"))

    for tile in tile_map.values():
        tile.draw(screen)

    if player:
        player.draw(screen)

    #key == pygame.KEYDOWN()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos 
            for tile in tile_map.values():
                tile.selected = False
            for tile in tile_map.values():
                if tile.handle_click(pos):
                    player = Player(tile.name[0], tile.name[1], "bob", (scale / 2), pygame.Color("red"), scale)
                    player.x = tile.x + (tile.size - player.size) / 2
                    player.y = tile.y + (tile.size - player.size) / 2
                    player.rect.topleft = (player.x, player.y)
                    print(f"{player.name} was moved to ({tile.x}, {tile.y})")
                    break
        elif event.type == pygame.KEYDOWN and player:
            if event.key == pygame.K_a:
                player.x -= player.scale
            elif event.key == pygame.K_d:
                player.x += player.scale
            elif event.key == pygame.K_w:
                player.y -= player.scale
            elif event.key == pygame.K_s:
                player.y += player.scale
            player.rect.topleft = (player.x, player.y)
        elif event.type == pygame.QUIT:
            running = False
    

    pygame.display.update()

pygame.quit()

