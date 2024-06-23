import pygame
from itertools import chain
WIDTH = 640
HEIGHT = 480
FPS = 30

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(f"Color: purple")
clock = pygame.time.Clock()

def truncline(text, font, maxwidth):
        real=len(text)       
        stext=text           
        l=font.size(text)[0]
        cut=0
        a=0                  
        done=1
        old = None
        while l > maxwidth:
            a=a+1
            n=text.rsplit(None, a)[0]
            if stext == n:
                cut += 1
                stext= n[:-cut]
            else:
                stext = n
            l=font.size(stext)[0]
            real=len(stext)               
            done=0                        
        return real, done, stext 

def wrapline(text, font, maxwidth): 
    done=0                      
    wrapped=[]                  
                               
    while not done:             
        nl, done, stext=truncline(text, font, maxwidth) 
        wrapped.append(stext.strip())                  
        text=text[nl:]                                 
    return wrapped

def wrap_multi_line(text, font, maxwidth):
    """ returns text taking new lines into account.
    """
    lines = chain(*(wrapline(line, font, maxwidth) for line in text.splitlines()))
    return list(lines)

color_rect = pygame.Rect(100, 100, WIDTH - 200, HEIGHT - 200)  
font = pygame.font.SysFont("Arial", 20, True)
msg = wrapline("Now is the count for all good men to come to the aid of their country", font, 120)
hover_surface = font.render(msg, True, pygame.Color("chartreuse"), pygame.Color("firebrick"))

hovering = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    mx, my = pygame.mouse.get_pos()
    screen.fill(pygame.Color("grey"))
    screen.fill(pygame.Color("purple"), color_rect)
    if color_rect.collidepoint((mx, my)):
        screen.blit(hover_surface, (mx, my))
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()