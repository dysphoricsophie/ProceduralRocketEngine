from cmath import rect
import pygame

pygame.init()
width, height = 1000,600
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
Blue = (0,0,255)
White = (255,255,255)
Gray = (200, 200, 200)
Dark_Gray = (20, 20, 20)
#-----------------------------------------------------------------------------------------------------------------------
btnw, btnh = 175, 75
h_btn = (screen.get_rect().center[0])/2
he_btn = (screen.get_rect().center[0])/2
btnw,btnh = int(btnw*h_btn/he_btn), int(btnh*h_btn/he_btn)
xs = screen.get_rect().center[0] - (btnw/2)
ys = 300
neil = [btnw, btnh, xs, ys]
jim_bob = tuple(neil)
button = pygame.Rect(jim_bob)

def main_render():
    screen.fill((Dark_Gray))
    pygame.draw.rect(screen, Gray, button)
    font_SIZE = 78
    h = (screen.get_height()+screen.get_width())/2
    he = (width+height)/2
    font = pygame.font.SysFont('Garamond', int(font_SIZE*h/he))
    textsurface = font.render('Rocket Engine Builder', False, Gray)  
    jim = textsurface.get_rect(center = screen.get_rect().center)
    jim[1] = 50
    screen.blit(textsurface, jim)
    pygame.display.update() 

def main():
    clock.tick(60)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False 
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if button.collidepoint(mouse_pos):
                    print('button was pressed at {0}'.format(mouse_pos))  
            if event.type == pygame.VIDEORESIZE:
                print(screen.get_rect().center)  
                btnw, btnh = 175, 75
                h_btn = (screen.get_rect().center[0])/2
                he_btn = (screen.get_rect().center[0])/2
                btnw,btnh = int(btnw*h_btn/he_btn), int(btnh*h_btn/he_btn)
                xs = screen.get_rect().center[0] - (btnw/2)
                ys = 300
                neil = [btnw, btnh, xs, ys]
                jim_bob = tuple(neil)
                button = pygame.Rect(jim_bob)                       
        main_render()        
    pygame.quit() 

if __name__ == "__main__":
    main()      
