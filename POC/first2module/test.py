import pygame

pygame.init()
pygame.font.init()
events = pygame.event.get()
for event in events:
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            print ('hello')