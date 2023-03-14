import pygame
import sys
import time

from model import Model
from view import View


class Controller:
    def __init__(self):
        self.numbers = [2, 5, 4, 8, 3, 6, 1, 2, 3, 4]
        self.number_cards = []
        self.code_blocks = []
        self.buttons = []
        self.surfaces = []

        self.model = Model(self)
        
        self.view = View(self)

    def register_number_cards(self, number_card):
        self.number_cards.append(number_card)
        self.surfaces.append(number_card)

    def register_code_block(self, code_block):
        self.surfaces.append(code_block)
        self.code_blocks.append(code_block)

    def register_button(self, button):
        self.surfaces.append(button)
        self.buttons.append(button)

    def check_exit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()



    def check_button_click(self):
        for button in self.buttons:
            if button.check_mouseclick():
                if button.text == "Play":
                    self.model.pause = False
                    self.model.manual_mode = False
                elif button.text == "Pause":
                    self.model.pause = True
                    #self.model.cleanup_rotation()
                elif button.text == "Prev" and not self.model.num_cards_handler.prev_next_disabled:
                    self.model.pause = True
                    self.model.cleanup_rotation()
                    self.model.manual_mode = True
                    self.model.undo_move()
                elif button.text == "Next" and not self.model.num_cards_handler.prev_next_disabled:
                    self.model.pause = True
                    self.model.cleanup_rotation(finish_rotation=True)
                    self.model.manual_mode = True
                    self.model.redo_move()

    def run(self):
        while True:
            self.check_exit()
            self.check_button_click()
            self.model.update()
            self.view.update()
            
            for surface in self.surfaces:
                surface.draw(self.view.canvas)
            pygame.display.update()
