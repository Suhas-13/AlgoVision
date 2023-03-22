import pygame
import sys
from .model import Model
from .view import View
from .enums import Algorithm
import src.menu as menu


class Controller:
    def __init__(self, algorithm=Algorithm.BUBBLE_SORT):
        self.numbers = ["7", "1", "8", "3", "5", "9", "4", "10", "6", "2"]
        self.code_blocks = []
        self.buttons = []
        self.button_handling = False
        self.reset_numbers = self.numbers.copy()
        self.surfaces = []
        self.current_algorithm = algorithm

        self.model = Model(self)
        self.view = View(self)

        self.allow_to_change = True
        self.started = False

        self.quit = False
        print(pygame.mouse.get_pressed()[0])


    def reset_all_cards(self):
        for i in range(10):
            # self.number_cards[i].text = self.reset_numbers[i]\
            self.model.num_cards_handler.number_cards[i].clicked = False
            self.model.num_cards_handler.number_cards[i].update(self.reset_numbers[i])
            self.model.num_cards_handler.number_cards[i].unhighlight()
            self.model.num_cards_handler.number_cards[i].typable = False
            self.model.num_cards_handler.number_cards[i].highlighted = False


    def update_reset_numbers(self):
        self.reset_numbers = self.numbers.copy()

    def register_number_cards(self, number_card):
        number_card.clicked = False
        self.model.num_cards_handler.number_cards.append(number_card)
        self.surfaces.append(number_card)
        self.buttons.append(number_card)

    def register_code_block(self, code_block):
        self.surfaces.append(code_block)
        self.code_blocks.append(code_block)

    def register_button(self, button):
        self.surfaces.append(button)
        self.buttons.append(button)

    def register_text(self, text):
        self.surfaces.append(text)

    def check_button_click(self):
        for button in self.buttons:
            if button.check_mouseclick():
                if button.text == "Play":
                    if not self.started:
                        self.started = True
                        self.model.start()
                    elif self.model.pause:
                        self.model.pause = False
                        self.started = True
                elif button.text == "Pause":
                    self.model.pause = True
                    # self.model.cleanup_rotation()
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
                elif button.text == "Reset":
                    self.started = False
                    self.reset_all_cards()
                    self.model.reset()
 

    def check_change_numbers(self, event):
        for number_card in self.model.num_cards_handler.number_cards:
            # set typalbe first
            number_card.check_typable()

            # then process keydown events
            if number_card.typable and event.type == pygame.KEYDOWN:
                number_card.type_in(event)
                self.numbers = [number_card.text for number_card in self.model.num_cards_handler.number_cards]
                self.update_reset_numbers()

    def check_events(self):
        for event in pygame.event.get():
            pygame.event.clear()
            if event.type == pygame.QUIT:
                self.quit = True
            if self.button_handling == False and event.type == pygame.MOUSEBUTTONDOWN:
                self.button_handling = True
                
            if self.button_handling:
                if 1024 <= event.type <= 1028:
                    self.check_button_click()
                
                if self.allow_to_change:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        for number_card in self.model.num_cards_handler.number_cards:
                            number_card.set_typable(False)
                self.check_change_numbers(event)

    def run(self):
        while True:
            # print(pygame.mouse.get_pressed()[0])
            self.check_events()
            if self.quit:
                break
            self.view.update()
            self.model.update()
            for surface in self.surfaces:
                surface.draw(self.view.canvas)
            pygame.display.update()
