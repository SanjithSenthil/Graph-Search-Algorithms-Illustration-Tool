import pygame

class Button(object):
    def __init__(self, x, y, width, height, text, text_color, background_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.text_color = text_color
        self.background_color = background_color
        self.angle = 0

    def check(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def draw(self, window):
        pygame.draw.rect(window, self.background_color, self.rect, 0, border_radius=10)
        draw_text_center(self.text, pygame.font.SysFont("CalibriBold", 25), window, self.x + self.width / 2, self.y + self.height / 2, self.text_color)
        pygame.draw.rect(window, self.background_color, self.rect, 3, border_radius=7)

def draw_text_center(text, font, screen, x, y, color):
    text_object = font.render(text, True, color)
    text_rectangle = text_object.get_rect(center=(int(x), int(y)))
    screen.blit(text_object, text_rectangle)

def draw_text(text, font, surface, x, y, color):
    text_object = font.render(text, 1, color)
    text_rectangle = text_object.get_rect()
    text_rectangle.topleft = (x, y)
    surface.blit(text_object, text_rectangle)