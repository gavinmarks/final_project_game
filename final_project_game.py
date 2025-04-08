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



def game_tiles(x_coordinate, y_coordinate):
    pygame.draw.rect(screen, pygame.Color("black"), pygame.Rect(x_coordinate, y_coordinate, 100, 100), 5)


running = True

while running:
    screen.fill(pygame.Color("white")) 

    for x, y in tile_cords:
        game_tiles(x, y)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()