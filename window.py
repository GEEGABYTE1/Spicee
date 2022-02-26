from doctest import script_from_examples
import pygame
from pygame.locals import *
import time

pygame.init()
screen = pygame.display.set_mode((640, 240))


next_blue = (88, 111, 124)
screen.fill(next_blue)
pygame.display.update()
base_caption = 'Spicee - Global ArticleDAO'
pygame.display.set_caption(base_caption)

# Printing Events

#KMOD_ALT, KMOD_RSHIFT, KMOD_LALT
key_dict = {K_1: (47, 69, 80), K_2: (184, 219, 217), K_3:(206, 219, 246)}
print(key_dict)


running = True
while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False 
        elif event.type == KEYDOWN:
            if event.key in key_dict:
                background = key_dict[event.key]
                screen.fill(background)
                pygame.display.update()

                caption = 'background color changed to = ' + str(background)
                pygame.display.set_caption(caption)
                time.sleep(0.2)
            if event.key == 1073741903:
                pygame.display.set_caption(base_caption)            # left arrow key


pygame.quit()


