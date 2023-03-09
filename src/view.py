import pygame

from constants import *


class Text:
    def __init__(self, text, x, y, size, draw_background=False, rect_color=None, rect_size=None):
        self.text = text
        self.font = pygame.font.SysFont('arial', size)
        self.draw_background = draw_background
        self.rect_color = rect_color
        self.rect_size = rect_size
        self.x = x
        self.y = y

        self.update(text)

        if self.draw_background:
            self.background_surface = pygame.Surface(self.rect_size)
            self.background_surface.fill(self.rect_color)
            self.background_surface.blit(self.text_surface,
                                         ((self.background_surface.get_width() - self.text_rect.width) // 2,
                                          (self.background_surface.get_height() - self.text_rect.height) // 2))
        else:
            self.background_surface = self.text_surface

        self.rect = self.background_surface.get_rect()
        self.rect.topleft = (self.x, self.y)

    def update(self, text):
        self.text = text
        self.text_surface = self.font.render(self.text, True, (0, 0, 0))
        self.text_rect = self.text_surface.get_rect()

    def draw(self, screen):
        screen.blit(self.background_surface, (self.x, self.y))  # draw text


class Button(Text):
    def __init__(self, text, x, y, size, draw_background=False, rect_color=None, rect_size=None):
        Text.__init__(self, text, x, y, size, draw_background, rect_color, rect_size)

        self.clicked = False

    def check_mouseclick(self):
        pos = pygame.mouse.get_pos()  # get mouse position

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] is True and self.clicked is False:
                self.clicked = True  # set to prevent double click
                return True

        if pygame.mouse.get_pressed()[0] is False:
            self.clicked = False  # set to prevent double click, while not pressing mouse, it is ready for next click




class NumCard(Text):
    

    def __init__(self, text, x, y, size):
        Text.__init__(self, text, x, y, size, True, LIGHT_GREY, (50, 50))
        # add border
        self.highlighted = False
        


    def moveto(self, x, y):
        self.x = x
        self.y = y

    def unhighlight(self):
        self.highlighted = False
        self.background_surface = pygame.Surface((self.rect_size[0], self.rect_size[1]))
        self.background_surface.fill(self.rect_color)
        self.background_surface.blit(self.text_surface,
                                     ((self.background_surface.get_width() - self.text_rect.width) // 2,
                                      (self.background_surface.get_height() - self.text_rect.height) // 2))
    def highlight(self):
        self.highlighted = True
        self.border = pygame.Surface((self.rect_size[0] + 2, self.rect_size[1] + 2))
        self.border.fill(GREEN)
        self.border.blit(self.background_surface, (1, 1))
        self.background_surface = self.border
        #self.background_surface.fill(GREEN)
    
class CodeBlock:
    def __init__(self, x, y, width, height, rect_color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect_color = rect_color

        self.background_surface = pygame.Surface((self.width, self.height))
        self.background_surface.fill(self.rect_color)

    def draw(self, screen):
        screen.blit(self.background_surface, (self.x, self.y))
    

        



class View:
    def __init__(self, controller):
        pygame.init()
        self.controller = controller
        self.canvas = pygame.display.set_mode((CANVAS_WIDTH, CANVAS_HEIGHT))
        self.canvas.fill(WHITE)
        pygame.display.set_caption("AlgoVision")

        self.init_number_cards(self.controller.numbers)
        self.init_code_blocks()
        self.init_buttons()

    def init_number_cards(self, num_arr):
        for idx, num in enumerate(num_arr):
            self.controller.register_number_cards(NumCard(str(num), CARD_X_POS[idx], CARD_Y_POS, 32))

    def init_code_blocks(self):
        self.controller.register_code_block(CodeBlock(25, 100, 375, 575, (0, 0, 0)))

    def init_buttons(self):
        self.controller.register_button(Button("Play", 25, 40, 24, True, LIGHT_GREY, (75, 40)))
        self.controller.register_button(Button("Pause", 125, 40, 24, True, LIGHT_GREY, (75, 40)))
        self.controller.register_button(Button("Last", 225, 40, 24, True, LIGHT_GREY, (75, 40)))
        self.controller.register_button(Button("Next", 325, 40, 24, True, LIGHT_GREY, (75, 40)))



    def update(self):
        self.canvas.fill(WHITE)
