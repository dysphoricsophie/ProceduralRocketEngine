import pygame 
import string
import random


pygame.init()

class Button:
    def __init__(self, title, pos, size):
        self.title = title
        self.pos = pos 
        self.surf = pygame.Surface(size)
        self.surf.fill("white")
        self.font = pygame.font.Font(None, size[0] // 6)
        self.text_surf = self.font.render(title, True, "black")
        self.rect = self.surf.get_rect(center=pos)
        self.text_rect = self.text_surf.get_rect(center=pos)

        self.is_clicked = False
        self.is_hovered = False
    
    def gen_password(self, n_chars: int, include_special: bool, include_capitals: bool):
        password = ""
        for _ in range(n_chars):
            choices = [string.ascii_lowercase]
            if include_special:
                choices.append(string.punctuation)
            if include_capitals:
                choices.append(string.ascii_uppercase)

            choice = random.choice(choices)
            char = random.choice(choice)
            password += char 
        
        return password

    def update(self, events, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

        self.is_clicked = False
        for event in events:
            if self.is_hovered and event.type == pygame.MOUSEBUTTONDOWN:
                self.is_clicked = True

        if self.is_hovered:
            self.surf.set_alpha(150)
        else:
            self.surf.set_alpha(255)

    def draw(self, screen):
        screen.blit(self.surf, self.rect)
        screen.blit(self.text_surf, self.text_rect)


def main():
    screen = pygame.display.set_mode((1100, 650))
    is_running = True 

    buttons = {
        "Random": ...,
        "Basic": ...,
        "Advanced": ...,
    }
    button_properties = {
        "Random": {
            "n_chars": 5,
            "include_special": False,
            "include_captials": False
        },
        "Basic": {
            "n_chars": 5,
            "include_special": False,
            "include_captials": True
        },
        "Advanced": {
            "n_chars": 5,
            "include_special": True,
            "include_captials": True
        },
    }

    button_size = (120, 40)

    for index, button_name in enumerate(buttons):
        buttons[button_name] = Button(
            button_name,
            (100, 100 + (button_size[1] + 10) * index),
            button_size
        )
    
    font = pygame.font.Font(None, 32)
    text = "InitialText"


    while is_running:
        events = pygame.event.get()
        mouse_pos = pygame.mouse.get_pos()

        for event in events:
            if event.type == pygame.QUIT:
                is_running = False 
        screen.fill((54, 52, 48))

        for button_name, button in buttons.items():
            button.update(events, mouse_pos)

            if button.is_clicked:
                print(button_name, "was clicked")

                args = button_properties[button_name].values()
                text = button.gen_password(*args)

            button.draw(screen)
        
        text_surf = font.render(text, True, "red")
        screen.blit(text_surf, (500, 500))

        pygame.display.flip()



if __name__ == "__main__":
    main()