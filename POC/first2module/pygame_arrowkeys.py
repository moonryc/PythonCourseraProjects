import pygame
import game_2048

# initialising pygame
pygame.init()

window_width = 600
window_height = 700

#                         w    h
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("a racing game by simply code")
test = TwentyFortyEight(4,4)
print (test)
running = True
while running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if keys[pygame.K_ESCAPE]:
            running = False
        elif keys[pygame.K_r]:
            print('Reset')
            test.reset
            print (test)
        elif keys[pygame.K_LEFT]:
            print('LEFT')
        elif keys[pygame.K_RIGHT]:
            print('RIGHT')
        elif keys[pygame.K_UP]:
            print('UP')
        elif keys[pygame.K_DOWN]:
            print('DOWN')
        # else:
        #     print(event)
            
pygame.quit()