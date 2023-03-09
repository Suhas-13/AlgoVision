import pygame
import sys
import time

from model import Model
from view import View


class Controller:
    def __init__(self):
        self.numbers = [6, 7, 8, 9, 10, 5, 4, 3, 1, 2]
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
                elif button.text == "Pause":
                    self.model.pause = True
                print(f"Button {button.text} clicked")

    def run(self):
        while True:
            self.check_exit()
            self.check_button_click()

            self.view.update()
            for surface in self.surfaces:
                surface.draw(self.view.canvas)
            self.model.update()

            pygame.display.update()
            #pygame.time.wait(5)
            #time.sleep(0.0167)
            #ime.sleep(0.0067)
