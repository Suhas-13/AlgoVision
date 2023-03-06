import pygame
import sys
import time

import model
from view import View


class Controller:
    def __init__(self):
        self.numbers = [6, 7, 8, 9, 10, 5, 4, 3, 2, 1]
        self.number_cards = []
        self.surfaces = []

        self.model = model.Model(self)
        self.view = View(self)

    def register_number_cards(self, number_card):
        self.number_cards.append(number_card)
        self.surfaces.append(number_card)

    def check_exit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def run(self):
        while True:
            self.check_exit()

            self.view.update()
            for surface in self.surfaces:
                surface.draw(self.view.canvas)
            self.model.update()

            pygame.display.update()
            time.sleep(0.0167)
