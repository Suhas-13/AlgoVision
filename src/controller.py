import pygame
import sys
import time

from model import Model
from view import View


class Controller:
    def __init__(self):
        self.numbers = ["7", "1", "8", "3", "5", "9", "4", "10", "6", "2"]
        self.number_cards = []
        self.code_blocks = []
        self.buttons = []
        self.surfaces = []

        self.model = Model(self)
        
        self.view = View(self)
        self.allow_to_change = True
        self.started = False


    def register_number_cards(self, number_card):
        self.number_cards.append(number_card)
        self.surfaces.append(number_card)
        self.buttons.append(number_card)

    def register_code_block(self, code_block):
        self.surfaces.append(code_block)
        self.code_blocks.append(code_block)

    def register_button(self, button):
        self.surfaces.append(button)
        self.buttons.append(button)

    def check_button_click(self):
        for button in self.buttons:
            if button.check_mouseclick():
                if button.text == "Play":
                    if not self.started:
                        self.started = True
                        self.model.start()
                    elif self.model.pause:
                        self.model.pause = False
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

    def check_change_numbers(self, event):
        for number_card in self.number_cards:
            # set typalbe first
            number_card.check_typable()

            # then process keydown events
            if number_card.typable and event.type == pygame.KEYDOWN:
                number_card.type_in(event)

    def check_events(self):
        self.check_button_click()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if self.allow_to_change:
                # set all number cards to not typable when mouse is clicked anywhere
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for number_card in self.number_cards:
                        number_card.set_typable(False)

                self.check_change_numbers(event)

    def run(self):
        while True:
            self.check_events()
            self.view.update()
            self.model.update()
            for surface in self.surfaces:
                surface.draw(self.view.canvas)
            pygame.display.update()
