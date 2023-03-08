from constants import *
from math import sin, cos, radians, sqrt


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

            card1.x, card1.y = CARD_X_POS[index1] + round(distance[0]), CARD_Y_POS + round(distance[1])
            card2.x, card2.y = CARD_X_POS[index2] - round(distance[0]), CARD_Y_POS - round(distance[1])

    def check_rotation_complete(self, index1, index2):
        card1, card2 = self.number_cards[index1], self.number_cards[index2]
        if card1.x < CARD_X_POS[index2] + 10 and card1.x > CARD_X_POS[index2] - 10:
            card1.moveto(CARD_X_POS[index2], CARD_Y_POS)
            card2.moveto(CARD_X_POS[index1], CARD_Y_POS)
            self.rotating = False
            self.timer = 0

            self.number_cards[index1], self.number_cards[index2] = card2, card1
            self.num_array[index1], self.num_array[index2] = self.num_array[index2], self.num_array[index1]


    def move_numbers(self, index1, index2):
        if not self.rotating:
            self.num_array[index1], self.num_array[index2] = self.num_array[index2], self.num_array[index1]
        self.rotation(index1, index2)

class SortingAlgor:
    def get_selection_sort_moves(self, array):
        moves = []
        for i in range(len(array)):
            min_idx = i
            for j in range(i + 1, len(array)):
                if array[j] < array[min_idx]:
                    min_idx = j
            array[i], array[min_idx] = array[min_idx], array[i]
            moves.append((i, min_idx))
        return moves
class Model:
    def __init__(self, controller):
        self.controller = controller
        self.num_cards_handler = NumberCardsHandler(self.controller.numbers, self.controller.number_cards)

        self.moves = SortingAlgor().get_selection_sort_moves(self.controller.numbers.copy())
        self.current_move = None
        self.current_move_idx = -1

        self.pause = True

    def update(self):
        if self.pause:
            return

        if not self.num_cards_handler.rotating:
            self.num_cards_handler.rotating = True

            if self.current_move_idx < 9:
                self.current_move_idx += 1
                self.current_move = self.moves[self.current_move_idx]

        self.num_cards_handler.move_numbers(self.current_move[0], self.current_move[1])
