


import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WINDOW_SIZE = (800, 600)
CELL_SIZE = 20
ERASER_SIZE = 40
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Eraser Canvas")

# Create a grid of blue cells
def create_grid():
    grid = []
    for y in range(0, WINDOW_SIZE[1], CELL_SIZE):
        for x in range(0, WINDOW_SIZE[0], CELL_SIZE):
            grid.append(pygame.Rect(x, y, CELL_SIZE, CELL_SIZE))
    return grid

# Main game loop
def main():
    grid = create_grid()
    eraser = pygame.Rect(0, 0, ERASER_SIZE, ERASER_SIZE)
    eraser_color = BLACK
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # Get mouse position and update eraser position
        mouse_pos = pygame.mouse.get_pos()
        eraser.x = mouse_pos[0] - ERASER_SIZE // 2
        eraser.y = mouse_pos[1] - ERASER_SIZE // 2
        
        # Erase cells that intersect with the eraser
        for cell in grid:
            if eraser.colliderect(cell):
                pygame.draw.rect(screen, WHITE, cell)
            else:
                pygame.draw.rect(screen, BLUE, cell)
        
        # Draw the eraser
        pygame.draw.rect(screen, eraser_color, eraser)
        
        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main() 