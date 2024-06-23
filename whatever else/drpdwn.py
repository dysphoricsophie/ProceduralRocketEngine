import pygame as pg

class DropDown():
    def __init__(self, color_menu, color_option, x, y, w, h, font, main, options):
        self.color_menu = color_menu
        self.color_option = color_option
        self.rect = pg.Rect(x, y, w, h)
        self.font = font
        self.main = main
        self.options = options
        self.draw_menu = False
        self.menu_active = False
        self.active_option = -1

    def draw(self, surf):
        pg.draw.rect(surf, self.color_menu[self.menu_active], self.rect, 0)
        msg = self.font.render(self.main, 1, (0, 0, 0))
        surf.blit(msg, msg.get_rect(center = self.rect.center))

        if self.draw_menu:
            for i, text in enumerate(self.options):
                rect = self.rect.copy()
                rect.y += (i+1) * self.rect.height
                pg.draw.rect(surf, self.color_option[1 if i == self.active_option else 0], rect, 0)
                msg = self.font.render(text, 1, (0, 0, 0))
                surf.blit(msg, msg.get_rect(center = rect.center))

    def update(self, event_list):
        mpos = pg.mouse.get_pos()
        self.menu_active = self.rect.collidepoint(mpos)
        
        self.active_option = -1
        for i in range(len(self.options)):
            rect = self.rect.copy()
            rect.y += (i+1) * self.rect.height
            if rect.collidepoint(mpos):
                self.active_option = i
                break

        if not self.menu_active and self.active_option == -1:
            self.draw_menu = False

        for event in event_list:
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                if self.menu_active:
                    self.draw_menu = not self.draw_menu
                elif self.draw_menu and self.active_option >= 0:
                    self.draw_menu = False
                    return self.active_option
        return -1

pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode((640, 480))

COLOR_INACTIVE = (200, 200, 200)
COLOR_ACTIVE = (165, 165, 165)
COLOR_LIST_INACTIVE = (182, 182, 182)
COLOR_LIST_ACTIVE = (172, 172, 172)

list1 = DropDown(
    [(200, 200, 200), (165, 165, 165)],
    [(182, 182, 182), (172, 172, 172)],
    (320-167), (240-25), 335, 50, 
    pg.font.SysFont(None, 30), 
    "Select the Purpose of the Engine", ["Lander", "Launcher", "SpaceTug"])

run = True
sock = ""
while run:
    clock.tick(30)
    event_list = pg.event.get()
    for event in event_list:
        if event.type == pg.QUIT:
            run = False
    selected_option = list1.update(event_list)
    if selected_option >= 0:
        sock = list1.options[selected_option]
        print(sock)
    screen.fill((20, 20, 20))
    list1.draw(screen)
    pg.display.flip() 
pg.quit()
exit()