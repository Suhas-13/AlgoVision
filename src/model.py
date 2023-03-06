
card_x_pos = [25 + 100 * i for i in range(10)]
class NumberCardsHandler:
    def __init__(self, num_array, number_cards):
        self.num_array = num_array
        self.number_cards = number_cards
        self.rotating = False

    def rotation(self, index1, index2):
        card1, card2 = self.number_cards[index1], self.number_cards[index2]
        if card1.x < card_x_pos[index2]:
            card1.x += 5
            card2.x -= 5
            self.rotating = True
        else:
            self.rotating = False
            self.number_cards[index1], self.number_cards[index2] = card2, card1

    def move_numbers(self, index1, index2):
        if not self.rotating:
            self.num_array[index1], self.num_array[index2] = self.num_array[index2], self.num_array[index1]
        self.rotation(index1, index2)

# class SortingAlgo:
#     def selection_sort(self, array, size):
#         numbers_handler = NumberCardsHandler(array)
#         for step in range(size):
#             min_idx = step
#
#             for i in range(step + 1, size):
#
#                 # to sort in descending order, change > to < in this line
#                 # select the minimum element in each loop
#                 if array[i] < array[min_idx]:
#                     min_idx = i
#
#             # put min at the correct position
#             yield step, min_idx

class Model:
    def __init__(self, controller):
        self.controller = controller
        self.num_cards_handler = NumberCardsHandler(self.controller.numbers, self.controller.number_cards)
        self.step = -1
        self.min_idx = 0

    def update(self):
        if not self.num_cards_handler.rotating:
            # modified version of selection sort algorithm
            if self.step < 9:
                self.step += 1
            self.min_idx = self.step
            for i in range(self.step + 1, len(self.controller.numbers)):
                if self.controller.numbers[i] < self.controller.numbers[self.min_idx]:
                    self.min_idx = i

        self.num_cards_handler.move_numbers(self.step, self.min_idx)

