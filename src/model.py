from constants import *
from math import sin, cos, radians, sqrt

card_x_pos = [SQUARE_SIZE / 2 + GAP * i for i in range(10)]


class NumberCardsHandler:
    def __init__(self, num_array, number_cards):
        self.num_array = num_array
        self.number_cards = number_cards
        self.rotating = False

        self.g = 2
        self.timer = 0
        self.r = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        self.angles = {1: 70, 2: 60, 3: 55, 4: 55, 5: 50, 6: 50, 7: 45, 8: 40, 9: 35}
        self.v0 = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        self.init_projectile_var()

    def init_projectile_var(self):
        for i in range(1, 10):
            self.r[i] = GAP * i
            self.v0[i] = sqrt((self.r[i] * self.g) / (sin(2 * radians(self.angles[i]))))

    def rotation(self, index1, index2):
        card1, card2 = self.number_cards[index1], self.number_cards[index2]
        self.check_rotation_complete(index1, index2)

        gap = index2 - index1
        if self.rotating and gap != 0:
            self.timer += 0.3
            distance = (self.v0[gap] * cos(radians(self.angles[gap])) * self.timer,
                        self.v0[gap] * sin(radians(self.angles[gap])) * self.timer - 0.5 * self.g * self.timer ** 2)

            card1.x, card1.y = card_x_pos[index1] + round(distance[0]), 300 + round(distance[1])
            card2.x, card2.y = card_x_pos[index2] - round(distance[0]), 300 - round(distance[1])

    def check_rotation_complete(self, index1, index2):
        card1, card2 = self.number_cards[index1], self.number_cards[index2]
        if card1.x < card_x_pos[index2] + 10 and card1.x > card_x_pos[index2] - 10:
            card1.moveto(card_x_pos[index2], 300)
            card2.moveto(card_x_pos[index1], 300)
            self.rotating = False
            self.number_cards[index1], self.number_cards[index2] = card2, card1
            self.num_array[index1], self.num_array[index2] = self.num_array[index2], self.num_array[index1]
            self.timer = 0

    def move_numbers(self, index1, index2):
        if not self.rotating:
            self.num_array[index1], self.num_array[index2] = self.num_array[index2], self.num_array[index1]
        self.rotation(index1, index2)


class Model:
    def __init__(self, controller):
        self.controller = controller
        self.num_cards_handler = NumberCardsHandler(self.controller.numbers, self.controller.number_cards)
        self.step = -1
        self.min_idx = 0

    def update(self):
        if not self.num_cards_handler.rotating:
            # modified version of selection sort algorithm
            self.num_cards_handler.rotating = True
            if self.step < 9:
                self.step += 1
            self.min_idx = self.step
            for i in range(self.step + 1, len(self.controller.numbers)):
                if self.controller.numbers[i] < self.controller.numbers[self.min_idx]:
                    self.min_idx = i

        self.num_cards_handler.move_numbers(self.step, self.min_idx)
