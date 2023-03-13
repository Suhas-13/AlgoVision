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

        if self.draw_background:
            self.background_surface = pygame.Surface(self.rect_size)
            self.background_surface.fill(self.rect_color)
            self.background_surface.blit(self.text_surface,
                                         ((self.background_surface.get_width() - self.text_rect.width) // 2,
                                          (self.background_surface.get_height() - self.text_rect.height) // 2))
        else:
            self.background_surface = self.text_surface

    def draw(self, screen):
        screen.blit(self.background_surface, (self.x, self.y))  # draw text


class Button(Text):
    def __init__(self, text, x, y, size, draw_background=False, rect_color=None, rect_size=None):
        Text.__init__(self, text, x, y, size,
                      draw_background, rect_color, rect_size)

        self.clicked = False

    def check_mouseclick(self):
        pos = pygame.mouse.get_pos()  # get mouse position

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] is True and self.clicked is False:
                self.clicked = True  # set to prevent double click
                return True

        if pygame.mouse.get_pressed()[0] is False:
            # set to prevent double click, while not pressing mouse, it is ready for next click
            self.clicked = False


class NumCard(Button):

    def __init__(self, text, x, y, size):
        Button.__init__(self, text, x, y, size, True, LIGHT_GREY, (SQUARE_SIZE, SQUARE_SIZE))
        # add border
        self.highlighted = False

        self.typable = False
        self.row = None

    def moveto(self, x, y):
        self.x = x
        self.y = y

    def unhighlight(self):
        self.highlighted = False
        self.update(self.text)

    def highlight(self, color):
        if self.highlighted:
            return
        self.highlighted = True
        self.border = pygame.Surface(
            (self.rect_size[0] + 2, self.rect_size[1] + 2))
        self.border.fill(color)
        self.border.blit(self.background_surface, (1, 1))
        self.background_surface = self.border

    def type_in(self, event):
        if event.key == pygame.K_RETURN:
            self.typable = False
            self.unhighlight()
            return
        if event.key == pygame.K_BACKSPACE:
            self.text = self.text[:-1]
        else:  # maximum length 2
            self.text += event.unicode if len(self.text) <= 1 else ""
        self.update(self.text)
        self.highlighted = False
        self.highlight(BLACK)

    def set_typable(self, typable):
        self.check_mouseclick()
        if not typable:
            self.typable = False
            self.unhighlight()
        elif typable:
            self.typable = True
            self.highlight(BLACK)
            print("Typable")

    def check_typable(self):
        self.check_mouseclick()
        if self.typable and self.clicked:
            self.set_typable(False)
        elif not self.typable and self.clicked:
            self.set_typable(True)

    def copy(self):
        return NumCard(self.text, self.x, self.y, 32)


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

        self.init_number_cards(self.controller.numbers, is_merge_sort=False)
        self.init_code_blocks()
        self.init_buttons()

    def init_number_cards(self, num_arr, is_merge_sort=False):
        if is_merge_sort:
            for idx, num in enumerate(num_arr):
                num_card = NumCard(str(num), MERGE_SORT_X_POS[0][idx], CARD_Y_POS[0], 32)
                num_card.row = 0
                self.controller.register_number_cards(num_card)
            return

        for idx, num in enumerate(num_arr):
            self.controller.register_number_cards(
                NumCard(str(num), CARD_X_POS[idx], CARD_Y_POS[2], 32))

    def init_code_blocks(self):
        self.controller.register_code_block(
            CodeBlock(25, 100, 375, 575, (0, 0, 0)))

    def init_buttons(self):
        self.controller.register_button(
            Button("Play", 25, 40, 24, True, LIGHT_GREY, (75, 40)))
        self.controller.register_button(
            Button("Pause", 125, 40, 24, True, LIGHT_GREY, (75, 40)))
        self.controller.register_button(
            Button("Last", 225, 40, 24, True, LIGHT_GREY, (75, 40)))
        self.controller.register_button(
            Button("Next", 325, 40, 24, True, LIGHT_GREY, (75, 40)))

    def update(self):
        self.canvas.fill(WHITE)
