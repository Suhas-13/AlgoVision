import pygame

from constants import *

card_x_pos = [25 + 100 * i for i in range(10)]
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

    def update(self, text):
        self.text = text
        self.text_surface = self.font.render(self.text, True, (0, 0, 0))
        self.text_rect = self.text_surface.get_rect()

    def draw(self, screen):
        screen.blit(self.background_surface, (self.x, self.y))  # draw text


class Button(Text):
    def __init__(self, text, x, y, size, rect_color):
        Text.__init__(self, text, x, y, size, rect_color)  # inheritance form Text class

        self.clicked = False

    def check_mouseclick(self):
        pos = pygame.mouse.get_pos()  # get mouse position

        if self.text_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] is True and self.clicked is False:
                self.clicked = True  # set to prevent double click
                return True

        if pygame.mouse.get_pressed()[0] is False:
            self.clicked = False  # set to prevent double click, while not pressing mouse, it is ready for next click

class NumCard(Text):
    def __init__(self, text, x, y, size):
        Text.__init__(self, text, x, y, size, True, (233, 233, 233), (50, 50))

    def moveto(self, x, y):
        self.x = x
        self.y = y
class View:
    def __init__(self, controller):
        pygame.init()
        self.controller = controller
        self.canvas = pygame.display.set_mode((CANVAS_WIDTH, CANVAS_HEIGHT))
        self.canvas.fill(WHITE)
        pygame.display.set_caption("AlgoVision")

        self.init_number_cards(self.controller.numbers)

        self.first_index, self.second_index = None, None

    def init_number_cards(self, num_arr):
        for idx, num in enumerate(num_arr):
            self.controller.register_number_cards(NumCard(str(num), card_x_pos[idx], 300, 32))

    # index1 has to be smaller than index2
    def rotation(self, index1, index2):
        card1, card2 = self.controller.number_cards[index1], self.controller.number_cards[index2]
        card1.move(index2)
        card2.move(index1)
        if card1.x == card_x_pos[index2] and card2.x == card_x_pos[index1]:
            self.controller.number_cards[index1], self.controller.number_cards[index2] = card2, card1
            self.first_index, self.second_index = None, None

    def update(self):
        self.canvas.fill(WHITE)
        # number_cards_val = [int(card.text) for card in self.controller.number_cards]
        #
        # if not self.controller.switching:
        #     for i in range(10):
        #         if number_cards_val[i] != self.controller.numbers[i]:
        #             if self.first_index is None:
        #                 self.first_index = i
        #             else:
        #                 self.second_index = i
        #
        # self.rotation(self.first_index, self.second_index)






