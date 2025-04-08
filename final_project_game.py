import pygame
import math

# Initialize Pygame
pygame.init()

# Window setup
WIDTH, HEIGHT = 1000, 750
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("super fun game")
clock = pygame.time.Clock()

# Hex settings
HEX_RADIUS = 40
HEX_HEIGHT = math.sqrt(3) * HEX_RADIUS
HEX_WIDTH = 2 * HEX_RADIUS
HORIZ_SPACING = HEX_WIDTH * 3/4
VERT_SPACING = HEX_HEIGHT

def hex_to_pixel(q, r):
    """Convert hex coordinates (q, r) to pixel coordinates (x, y)."""
    x = HEX_RADIUS * (3/2 * q)
    y = HEX_RADIUS * (math.sqrt(3) * (r + q / 2))
    return x, y

def draw_hex(center_x, center_y, color=(200, 200, 200), border_color=(0, 0, 0)):
    """Draw a single hex at (center_x, center_y)."""
    points = []
    for i in range(6):
        angle = math.radians(60 * i)  # Pointy-top
        x_i = center_x + HEX_RADIUS * math.cos(angle)
        y_i = center_y + HEX_RADIUS * math.sin(angle)
        points.append((x_i, y_i))
    pygame.draw.polygon(screen, color, points)
    pygame.draw.polygon(screen, border_color, points, 2)

# Main loop
running = True
cols, rows = 5, 5  # Grid size

while running:
    screen.fill((30, 30, 30))  # Background color

    for q in range(cols):
        for r in range(rows):
            x, y = hex_to_pixel(q, r)
            #x += 100  # Padding
            #y -= 200
            draw_hex(x, y)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()