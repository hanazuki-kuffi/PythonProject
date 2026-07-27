import pygame
from sys import exit

#game variables
GAME_WIDTH = 666
GAME_HEIGHT = 375

#game images
backround_images = pygame.image.load("flappyaquaplace.png")

def draw():
    window.blit(backround_images, (0, 0))

pygame.init()
window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption("Flappy Aqua")
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    draw()
    pygame.display.update()
    clock.tick(60)
