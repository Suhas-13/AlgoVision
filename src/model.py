from constants import *
from math import sin, cos, radians, sqrt
from sorting import SelectionSort, InsertionSort, BubbleSort, NumberCardOperations
import pygame
import time


class NumberCardsHandler:
    def __init__(self, num_array, number_cards):
        self.num_array = num_array
        self.number_cards = number_cards
        self.rotating = False
        self.time_since_rotation = 0

        self.g = 2
        self.timer = 0
        self.r = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        self.angles = {1: 70, 2: 60, 3: 55, 4: 55,
                       5: 50, 6: 50, 7: 45, 8: 40, 9: 35}
        self.v0 = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        self.init_projectile_var()

    def init_projectile_var(self):
        for i in range(1, 10):
            self.r[i] = GAP * i
            self.v0[i] = sqrt((self.r[i] * self.g) /
                              (sin(2 * radians(self.angles[i]))))

    def rotation(self, index1, index2):
        card1, card2 = self.number_cards[index1], self.number_cards[index2]
        self.check_rotation_complete(index1, index2)
        gap = index2 - index1
        if self.rotating and gap != 0:
            self.timer += 0.3
            distance = (self.v0[gap] * cos(radians(self.angles[gap])) * self.timer,
                        self.v0[gap] * sin(radians(self.angles[gap])) * self.timer - 0.5 * self.g * self.timer ** 2)

            card1.x, card1.y = CARD_X_POS[index1] + \
                round(distance[0]), CARD_Y_POS + round(distance[1])
            card2.x, card2.y = CARD_X_POS[index2] - \
                round(distance[0]), CARD_Y_POS - round(distance[1])

    def check_rotation_complete(self, index1, index2):
        card1, card2 = self.number_cards[index1], self.number_cards[index2]
        if card1.x < CARD_X_POS[index2] + 6 and card1.x > CARD_X_POS[index2] - 6:
            card1.moveto(CARD_X_POS[index2], CARD_Y_POS)
            card2.moveto(CARD_X_POS[index1], CARD_Y_POS)
            self.rotating = False
            self.time_since_rotation = 0
            self.timer = 0
            self.number_cards[index1], self.number_cards[index2] = card2, card1
            self.num_array[index1], self.num_array[index2] = self.num_array[index2], self.num_array[index1]

    def move_numbers(self, index1, index2):
        if not self.rotating:
            self.num_array[index1], self.num_array[index2] = self.num_array[index2], self.num_array[index1]
        self.rotation(index1, index2)
        # highlight the cards


class Model:
    def __init__(self, controller):
        self.controller = controller
        self.num_cards_handler = NumberCardsHandler(
            self.controller.numbers, self.controller.number_cards)
        self.moves = SelectionSort(self.controller.numbers.copy()).get_moves()
        self.current_move = None
        self.current_move_idx = 0

        self.pause = True
        self.prev_move = None

    def update(self):

        if self.pause:
            return

        self.num_cards_handler.time_since_rotation += 1
        if self.num_cards_handler.time_since_rotation < 10:
            return

        if not self.num_cards_handler.rotating:
            if self.current_move_idx == len(self.moves):
                self.pause = True
                self.current_move_idx = 0
                return
            self.current_move = self.moves[self.current_move_idx]
            if self.prev_move is not None and self.prev_move[0] == NumberCardOperations.COMPARE:
                if self.current_move[0] == NumberCardOperations.SWAP:
                    pygame.time.delay(1000)
                self.controller.number_cards[self.prev_move[1]].unhighlight()
                self.controller.number_cards[self.prev_move[2]].unhighlight()

            if self.current_move[0] == NumberCardOperations.SWAP:
                self.num_cards_handler.move_numbers(
                    self.current_move[1], self.current_move[2])
                self.num_cards_handler.rotating = True
            elif self.current_move[0] == NumberCardOperations.COMPARE:
                self.controller.number_cards[self.current_move[1]].highlight()
                self.controller.number_cards[self.current_move[2]].highlight()
                pygame.time.delay(400)
            self.prev_move = self.current_move
            self.current_move_idx += 1
        else:
            self.num_cards_handler.rotation(
                self.current_move[1], self.current_move[2])
