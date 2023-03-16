from constants import *
from math import sin, cos, radians, sqrt
from sorting import SelectionSort, InsertionSort, BubbleSort, NumberCardOperations, MergeSort
import pygame
import time


class NumberCardsHandler:
    def __init__(self, number_cards):
        self.number_cards = number_cards
        self.rotating = False
        self.prev_next_disabled = False


        self.time_since_rotation = 0
        self.rows = {0: number_cards, 1: [None] * 10, 2: [None] * 10, 3: [None] * 10, 4: [None] * 10}

        self.g = 2
        self.timer = 0
        self.r = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        self.angles = {1: 70, 2: 60, 3: 55, 4: 55,
                       5: 50, 6: 50, 7: 45, 8: 40, 9: 35}
        self.v0 = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        self.init_projectile_var()

        self.slope = None

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
                               round(distance[0]), CARD_Y_POS[2] + round(distance[1])
            card2.x, card2.y = CARD_X_POS[index2] - \
                               round(distance[0]), CARD_Y_POS[2] - round(distance[1])

    def check_rotation_complete(self, index1, index2):
        card1, card2 = self.number_cards[index1], self.number_cards[index2]
        if card1.x < CARD_X_POS[index2] + 6 and card1.x > CARD_X_POS[index2] - 6:
            card1.moveto(CARD_X_POS[index2], CARD_Y_POS[2])
            card2.moveto(CARD_X_POS[index1], CARD_Y_POS[2])
            self.rotating = False
            self.time_since_rotation = 0
            self.timer = 0
            self.number_cards[index1], self.number_cards[index2] = card2, card1
            self.prev_next_disabled = False

    def undo_rotation_immediately(self, index1, index2, reverse = False):
        card1, card2 = self.number_cards[index1], self.number_cards[index2]
        if reverse:
            card1.moveto(CARD_X_POS[index2], CARD_Y_POS)
            card2.moveto(CARD_X_POS[index1], CARD_Y_POS)
            self.number_cards[index1], self.number_cards[index2] = card2, card1
            self.num_array[index1], self.num_array[index2] = self.num_array[index2], self.num_array[index1]
        else:
            card1.moveto(CARD_X_POS[index1], CARD_Y_POS)
            card2.moveto(CARD_X_POS[index2], CARD_Y_POS)
            self.number_cards[index1], self.number_cards[index2] = card2, card1
            self.num_array[index1], self.num_array[index2] = self.num_array[index2], self.num_array[index1]

    def move_numbers(self, index1, index2):
        self.prev_next_disabled = True
        self.rotation(index1, index2)

    def copy_and_divide(self, index1, index2, controller):
        current_row = self.number_cards[index1].row
        for i in range(index1, index2 + 1):
            self.number_cards[i].row += 1
            new_card = self.number_cards[i].copy()
            new_card.row = current_row + 1
            self.rows[new_card.row][i] = new_card
            new_card.moveto(MERGE_SORT_X_POS[new_card.row][i], CARD_Y_POS[new_card.row])
            controller.surfaces.append(new_card)

    def merge(self, index1, index2, controller):
        current_row = self.number_cards[index1].row
        num_card1, num_card2 = self.rows[current_row - 1][index1], self.rows[current_row][index2]
        self.check_merge_complete(index1, num_card1, num_card2, controller)
        sign = 1 if num_card2.x > num_card1.x else -1

        if self.rotating:
            num_card2.x -= self.timer * sign
            num_card2.y += self.timer * self.slope * sign
            self.timer += 0.01

    def set_slope(self, index1, index2):
        current_row = self.number_cards[index1].row
        num_card1, num_card2 = self.rows[current_row - 1][index1], self.rows[current_row][index2]
        self.slope = - (num_card2.y - num_card1.y) / (num_card2.x - num_card1.x)

    def check_merge_complete(self, index1, num_card1, num_card2, controller):
        if abs(num_card2.x - num_card1.x) < 1:
            num_card2.moveto(num_card1.x, num_card1.y)
            self.rotating = False
            self.time_since_rotation = 0
            self.timer = 0
            num_card1.update(num_card2.text)
            controller.surfaces.remove(num_card2)
            self.number_cards[index1].row -= 1

    def clear(self, index1, index2):
        current_row = self.number_cards[index1].row
        for i in range(index1, index2 + 1):
            self.rows[current_row - 1][i].update("")

    def copy_and_divide(self, index1, index2, controller):
        current_row = self.number_cards[index1].row
        for i in range(index1, index2 + 1):
            self.number_cards[i].row += 1
            new_card = self.number_cards[i].copy()
            new_card.row = current_row + 1
            self.rows[new_card.row][i] = new_card
            new_card.moveto(MERGE_SORT_X_POS[new_card.row][i], CARD_Y_POS[new_card.row])
            controller.surfaces.append(new_card)

    def merge(self, index1, index2, controller):
        current_row = self.number_cards[index1].row
        num_card1, num_card2 = self.rows[current_row - 1][index1], self.rows[current_row][index2]
        self.check_merge_complete(index1, num_card1, num_card2, controller)
        sign = 1 if num_card2.x > num_card1.x else -1

        if self.rotating:
            num_card2.x -= self.timer * sign
            num_card2.y += self.timer * self.slope * sign
            self.timer += 0.01

    def set_slope(self, index1, index2):
        current_row = self.number_cards[index1].row
        num_card1, num_card2 = self.rows[current_row - 1][index1], self.rows[current_row][index2]
        self.slope = - (num_card2.y - num_card1.y) / (num_card2.x - num_card1.x)

    def check_merge_complete(self, index1, num_card1, num_card2, controller):
        if abs(num_card2.x - num_card1.x) < 1:
            num_card2.moveto(num_card1.x, num_card1.y)
            self.rotating = False
            self.time_since_rotation = 0
            self.timer = 0
            num_card1.update(num_card2.text)
            controller.surfaces.remove(num_card2)
            self.number_cards[index1].row -= 1

    def clear(self, index1, index2):
        current_row = self.number_cards[index1].row
        for i in range(index1, index2 + 1):
            self.rows[current_row - 1][i].update("")


class Model:
    def __init__(self, controller):
        self.controller = controller
        self.num_cards_handler = NumberCardsHandler(self.controller.number_cards)
        self.moves = None
        self.current_move = None

        self.prev_move_stack = []
        self.next_move_stack = list(reversed(self.moves))
        self.pause = True
        self.manual_mode = False

    def cleanup_rotation(self, finish_rotation = False):
        if self.num_cards_handler.rotating:
            if self.get_last_move() is not None:
                current_move = self.prev_move_stack.pop()
                self.next_move_stack.append(current_move)
                self.num_cards_handler.undo_rotation_immediately(
                        current_move[1], current_move[2], reverse = finish_rotation)
            self.num_cards_handler.rotating = False


    def get_last_move(self):
        if len(self.prev_move_stack) == 0:
            return None
        return self.prev_move_stack[-1]

    def get_next_move(self):
        if len(self.next_move_stack) == 0:
            return None
        return self.next_move_stack[-1]

    def clear_highlight(self, move):
        if move is None:
            return
        if move[0] == NumberCardOperations.COMPARE:
            self.controller.number_cards[move[1]].unhighlight()
            self.controller.number_cards[move[2]].unhighlight()

    def highlight(self, move):
        if move[0] == NumberCardOperations.COMPARE:
            self.controller.number_cards[move[1]].highlight()
            self.controller.number_cards[move[2]].highlight()

    def redo_move(self):
        if len(self.next_move_stack) == 0:
            return
        self.cleanup_rotation(finish_rotation = True)

        
        last_move = self.get_last_move()
        print("Last Move is " + str(last_move))
        if last_move is None:
            return
        if last_move[0] == NumberCardOperations.COMPARE:
            self.clear_highlight(last_move)
        if len(self.next_move_stack) == 0:
            return
        current_move = self.next_move_stack.pop()
        self.prev_move_stack.append(current_move)
        if current_move[0] == NumberCardOperations.SWAP:
            self.num_cards_handler.move_numbers(current_move[1], current_move[2])
            self.num_cards_handler.rotating = True
        elif current_move[0] == NumberCardOperations.COMPARE:
            self.highlight(current_move)
        

    def undo_move(self):
        if len(self.prev_move_stack) == 0:
            return
        current_move = self.get_next_move()
        if current_move is not None and current_move[0] == NumberCardOperations.COMPARE:
            self.clear_highlight(current_move)

        current_move = self.prev_move_stack.pop()
        self.next_move_stack.append(current_move)

        if current_move[0] == NumberCardOperations.SWAP:
            self.num_cards_handler.move_numbers(current_move[1], current_move[2])
            self.num_cards_handler.rotating = True
        elif current_move[0] == NumberCardOperations.COMPARE:
            self.highlight(current_move)
        
    def update(self):
        if self.controller.allow_to_change:
            self.change_numbers()

        if self.manual_mode and self.get_last_move() is not None:
            current_move = self.get_last_move()
            self.num_cards_handler.rotation(
                current_move[1], current_move[2])
            return

        if self.pause and not self.num_cards_handler.rotating:
            self.clear_highlight(self.get_last_move())
            return

        self.num_cards_handler.time_since_rotation += 1
        if self.num_cards_handler.time_since_rotation < 10:
            return
        
        if not self.num_cards_handler.rotating:
            if len(self.next_move_stack) == 0:
                self.pause = True
                for card in self.controller.number_cards:
                    card.unhighlight()
              
                #self.current_move_idx = 0
                return
            prev_move = self.get_last_move()
            current_move = self.next_move_stack.pop()
            self.prev_move_stack.append(current_move)
            if prev_move is not None and prev_move[0] == NumberCardOperations.COMPARE:
                    if current_move[0] == NumberCardOperations.SWAP:
                        pygame.time.delay(200)
                    self.clear_highlight(prev_move)
            if current_move[0] == NumberCardOperations.SWAP:
                self.num_cards_handler.move_numbers(
                    current_move[1], current_move[2])
                self.num_cards_handler.rotating = True
            elif current_move[0] == NumberCardOperations.COMPARE:
                self.highlight(GREENcurrent_moveGREEN)
                pygame.time.delay(400)

            elif self.current_move[0] == NumberCardOperations.DIVIDE:
                self.num_cards_handler.copy_and_divide(self.current_move[1], self.current_move[2], self.controller)
                pygame.time.delay(400)

            elif self.current_move[0] == NumberCardOperations.MERGE:
                self.num_cards_handler.rotating = True
                self.num_cards_handler.set_slope(self.current_move[1], self.current_move[2])
                self.num_cards_handler.merge(self.current_move[1], self.current_move[2], self.controller)

            elif self.current_move[0] == NumberCardOperations.CLEAR:
                self.num_cards_handler.clear(self.current_move[1], self.current_move[2])
                pygame.time.delay(150)

    
        else:
            current_move = self.get_last_move()
            if current_move[0] == NumberCardOperations.SWAP:
                self.num_cards_handler.rotation(
                    current_move[1], current_move[2])
            elif current_move[0] == NumberCardOperations.MERGE:
                self.num_cards_handler.merge(current_move[1], current_move[2], self.controller)

