import sys
import pygame
from pygame.locals import QUIT, Rect

pygame.init()
surface = pygame.display.set_mode((800, 800))
fpsclock = pygame.time.Clock()
pygame.display.set_caption('pygame_rect_test')

def main():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        surface.fill((255,255,255))