import pygame
import pygame.font

pygame.init()
font = pygame.font.SysFont(None, 50)
text = font.render('Hello World', True, (255, 0, 0))

window = pygame.display.set_mode((600, 300), pygame.RESIZABLE)
clock = pygame.time.Clock()

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill(0)
    window.blit(text, text.get_rect(center = window.get_rect().center))
    pygame.display.flip()

pygame.quit()
exit()