import sys
import webbrowser
import pygame
from pygame.rect import Rect

class TextInputBox(pygame.sprite.Sprite):
    def __init__(self, x, y, w, font):
        super().__init__()
        self.color = (255, 255, 255)
        self.backcolor = None
        self.pos = (x, y) 
        self.width = w
        self.font = font
        self.active = False
        self.text = ""
        self.render_text()

    def render_text(self):
        t_surf = font.render(self.text, True, self.color, self.backcolor)
        self.image = pygame.Surface((max(self.width, t_surf.get_width()+10), t_surf.get_height()+10), pygame.SRCALPHA)
        if self.backcolor:
            self.image.fill(self.backcolor)
        self.image.blit(t_surf, (5, 5))
        pygame.draw.rect(self.image, self.color, self.image.get_rect().inflate(-2, -2), 2)
        self.rect = self.image.get_rect(topleft = self.pos)

    def update(self, event_list):
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN and not self.active:
                self.active = self.rect.collidepoint(event.pos)
            if event.type == pygame.KEYDOWN and self.active:
                if event.key == pygame.K_RETURN:
                    self.active = False
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.render_text()

pygame.init()
        
width, height = 1000, 600
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))
Blue = (0,0,255)
White = (255,255,255)
Light_Blue = (180, 221, 255)
Gray = (200, 200, 200)
Dark_Gray = (20, 20, 20)
#------------------------------------------------------------------
Btn_sps = 10
cntrx = (width/6)

# main button
btnw1, btnh1 = 220, 75
xs1 = cntrx - (btnw1/2)
ys1 = 200
neil1 = [xs1, ys1, btnw1, btnh1]
jim_bob1 = tuple(neil1)
random_gen = pygame.Rect(jim_bob1)
#------------------------------------------------------------------
btnw2, btnh2 = 220, 75
xs2 = cntrx - (btnw2/2)
ys2 = ys1 + 85
neil2 = [xs2, ys2, btnw2, btnh2]
jim_bob2 = tuple(neil2)
basic_gen = pygame.Rect(jim_bob2)
#------------------------------------------------------------------
btnw3, btnh3 = 220, 75
xs3 = cntrx - (btnw3/2)
ys3 = ys2 + 85
neil3 = [xs3, ys3, btnw3, btnh3]
jim_bob3 = tuple(neil3)
advanced_gen = pygame.Rect(jim_bob3)

# credits + guide
btnw4, btnh4 = 103, 42
xs4 = (cntrx - 57) - (btnw4/2)
ys4 = ys3 + 85
neil4 = [xs4, ys4, btnw4, btnh4]
jim_bob4 = tuple(neil4)
guide = pygame.Rect(jim_bob4)
#------------------------------------------------------------------
btnw5, btnh5 = 103, 42
xs5 = (cntrx + 57) - (btnw5/2)
ys5 = ys3 + 85
neil5 = [xs5, ys5, btnw5, btnh5]
jim_bob5 = tuple(neil5)
credits = pygame.Rect(jim_bob5)

# exit
btnw6, btnh6 = 50, 20
xs6 = 10
ys6 = 572
neil6 = [xs6, ys6, btnw6, btnh6]
jim_bob6 = tuple(neil6)
exit_btn = pygame.Rect(jim_bob6)

# social media
imp1 = pygame.image.load("/Assets/reddit.png")
btnw8, btnh8 = 40, 40
imp1 = pygame.transform.scale(imp1, (btnw8, btnh8))
xs8 = 882 - (btnw8)
ys8 = 585 - (btnh8)
neil8 = [xs8, ys8, btnw8, btnh8]
jim_bob8 = tuple(neil8)
#------------------------------------------------------------------
imp2 = pygame.image.load("/Assets/discord.png")
btnw9, btnh9 = 40, 40
imp2 = pygame.transform.scale(imp2, (btnw9, btnh9))
xs9 = (xs8 + (btnw9+Btn_sps))
ys9 = 585 - (btnh9)
neil9 = [xs9, ys9, btnw9, btnh9]
jim_bob9 = tuple(neil9)
#------------------------------------------------------------------
imp3 = pygame.image.load("/Assets/website.png")
btnw10, btnh10 = 40, 40
imp3 = pygame.transform.scale(imp3, (btnw10, btnh10))
xs10 = (xs9 + (btnw10+Btn_sps))
ys10 = 585 - (btnh10)
neil10 = [xs10, ys10, btnw10, btnh10]
jim_bob10 = tuple(neil10)
#------------------------------------------------------------------
reddit_btn = screen.blit(imp1, jim_bob8)
discord_btn = screen.blit(imp2, jim_bob9)
web_btn = screen.blit(imp3, jim_bob10)

def render(jesus):
    screen.fill((Dark_Gray))
    pygame.draw.rect(screen, Gray, random_gen)
    pygame.draw.rect(screen, Gray, basic_gen)
    pygame.draw.rect(screen, Gray, advanced_gen)
    pygame.draw.rect(screen, Gray, guide)
    pygame.draw.rect(screen, Gray, credits)
    pygame.draw.rect(screen, Gray, exit_btn)
    reddit_btn = screen.blit(imp1, jim_bob8)
    discord_btn = screen.blit(imp2, jim_bob9)
    web_btn = screen.blit(imp3, jim_bob10)
    #------------------------------------------------------------------
    (x, y, width, height) = (360, 158, 620, 370)
    border_width = 3
    pygame.draw.rect(screen, Dark_Gray, (x, y, width, height))
    pygame.draw.rect(screen, Gray, (x, y, width, height), width=border_width)
    #-------------------------------------------------------------------
    font1 = pygame.font.SysFont("Garamond", 90)
    textsurface1 = font1.render("Rocket Engine Builder", False, Gray)  
    jim1 = textsurface1.get_rect(center = screen.get_rect().center)
    jim1[1] = 28
    screen.blit(textsurface1, jim1)
    #-------------------------------------------------------------------
    font2 = pygame.font.SysFont("Arial", 19, True)
    textsurface2 = font2.render("Choose a configuration:", False, Gray)    
    jim2 = textsurface2.get_rect(center = screen.get_rect().center)
    jim2[0] = 55
    jim2[1] = 164
    screen.blit(textsurface2, jim2)
    #-------------------------------------------------------------------
    font2 = pygame.font.SysFont("Arial", 18)
    textsurface2 = font2.render("Random Generation", False, Dark_Gray)  
    jim2 = textsurface2.get_rect(center = screen.get_rect().center)
    jim2[0] = cntrx - 80
    jim2[1] = ys1 + 25
    screen.blit(textsurface2, jim2)    
    #-------------------------------------------------------------------
    font2 = pygame.font.SysFont("Arial", 18)
    textsurface2 = font2.render("Basic Generation", False, Dark_Gray)  
    jim2 = textsurface2.get_rect(center = screen.get_rect().center)
    jim2[0] = cntrx - 71
    jim2[1] = ys1 + 110
    screen.blit(textsurface2, jim2)      
    #-------------------------------------------------------------------
    font2 = pygame.font.SysFont("Arial", 18)
    textsurface2 = font2.render("Advanced Generation", False, Dark_Gray)  
    jim2 = textsurface2.get_rect(center = screen.get_rect().center)
    jim2[0] = cntrx - 86
    jim2[1] = ys2 + 111
    screen.blit(textsurface2, jim2) 
    #------------------------------------------------------------------- 
    jimy2 = [675,133]
    font4 = pygame.font.SysFont("Arial", 20)
    textsurface4 = font4.render(jesus, False, Gray) 
    jimy2[0] = (jimy2[0] - (textsurface4.get_width()/2))
    screen.blit(textsurface4, jimy2)           
    #-------------------------------------------------------------------
    font3 = pygame.font.SysFont("Garamond", 22)
    textsurface3 = font3.render("EXIT", False, Dark_Gray)
    jim3 = [17,575]
    screen.blit(textsurface3, jim3)        
    #-------------------------------------------------------------------
    pygame.display.flip() 

font = pygame.font.SysFont(None, 100)
text_input_box = TextInputBox(610, 500, 200, font)
group = pygame.sprite.Group(text_input_box)

def main():
    clock.tick(60)
    run = True
    jesus = "Press a button on your right to start..."
    while run:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                run = False 
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos 
                if random_gen.collidepoint(mouse_pos):     
                    jesus = "Random Generation"                 
                    print("The random generation button was pressed")
                    #-------------------------------------------------------------------  
                if basic_gen.collidepoint(mouse_pos):
                    jesus = "Basic Generation"
                    print("The basic generation was pressed")
                    #-------------------------------------------------------------------
                if advanced_gen.collidepoint(mouse_pos):
                    jesus = "Advanced Geneneration"
                    print("The advanced generation was pressed")
                    #-------------------------------------------------------------------    
                if guide.collidepoint(mouse_pos):
                    jesus = "Help Guide"
                    print("The guide button was pressed")
                if credits.collidepoint(mouse_pos):
                    jesus = "Credits"
                    print("The credits button was pressed")                    
                if reddit_btn.collidepoint(mouse_pos):
                    print("The reddit button was pressed")
                    webbrowser.open(r"https://reddit.com/")    
                if discord_btn.collidepoint(mouse_pos):
                    print("The discord button was pressed")
                    webbrowser.open(r"https://youtube.com/")    
                if web_btn.collidepoint(mouse_pos):
                    print("The website button was pressed")
                    webbrowser.open(r"https://stackoverflow.com/")      
                if exit_btn.collidepoint(mouse_pos):
                    print("The exit button was pressed")
                    sys.exit()  
        group.update(events)
        group.draw(screen)                                                                                      
        render(jesus)        
    pygame.quit()
    
main()