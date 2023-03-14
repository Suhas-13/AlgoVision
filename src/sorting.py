from abc import ABC, abstractmethod
from random import randint, shuffle

import random


class NumberCardOperations:
    SWAP: int = 1
    COMPARE: int = 2

    @staticmethod
    def create_swap_operation(index1: int, index2: int) -> tuple:
        min_index = min(index1, index2)
        max_index = max(index1, index2)
        return (NumberCardOperations.SWAP, min_index, max_index)

    @staticmethod
    def create_compare_operation(index1: int, index2: int) -> tuple:
        min_index = min(index1, index2)
        max_index = max(index1, index2)
        return (NumberCardOperations.COMPARE, min_index, max_index)

    @staticmethod
    def create_highlight_operation(index: int) -> tuple:
        return (NumberCardOperations.HIGH_LIGHT, index)


class SortingAlgorithm(ABC):

    @abstractmethod
    def __init__(self, array):
        self.array = array

    @abstractmethod
    def get_moves(self):
        moves = []
        return moves


class SelectionSort(SortingAlgorithm):
    def __init__(self, array):
        super().__init__(array)

    def get_moves(self):
        moves = []
        for i in range(len(self.array)):
            min_idx = i
            for j in range(i + 1, len(self.array)):
                moves.append(
                    NumberCardOperations.create_compare_operation(j, i))
                if self.array[j] < self.array[min_idx]:
                    min_idx = j
            self.array[i], self.array[min_idx] = self.array[min_idx], self.array[i]
            moves.append(
                NumberCardOperations.create_compare_operation(i, min_idx))
            moves.append(
                NumberCardOperations.create_swap_operation(i, min_idx))
        return moves


class InsertionSort(SortingAlgorithm):
    def __init__(self, array):
        super().__init__(array)

    def get_moves(self):
        moves = []
        for i in range(1, len(self.array)):
            key = self.array[i]
            j = i - 1
            moves.append(NumberCardOperations.create_compare_operation(i, j))
            while j >= 0 and key < self.array[j]:
                self.array[j + 1] = self.array[j]
                moves.append(
                    NumberCardOperations.create_compare_operation(i, j))
                moves.append(
                    NumberCardOperations.create_compare_operation(i, j))
                moves.append(
                    NumberCardOperations.create_swap_operation(j, j + 1))
                j -= 1
            self.array[j + 1] = key
        return moves


class BubbleSort(SortingAlgorithm):
    def __init__(self, array):
        super().__init__(array)

    def get_moves(self):
        moves = []
        n = len(self.array)
        for i in range(n):
            for j in range(0, n - i - 1):
                moves.append(
                    NumberCardOperations.create_compare_operation(j, j + 1))
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j +
                                              1] = self.array[j + 1], self.array[j]
                    moves.append(
                        NumberCardOperations.create_compare_operation(j, j + 1))
                    moves.append(
                        NumberCardOperations.create_swap_operation(j, j + 1))
        return moves

class BogoSort(SortingAlgorithm):
    def __init__(self, array):
        super().__init__(array)

    def get_moves(self):
        moves = []
        solution = sorted(self.array)
        current = self.array.copy()

        while current != solution:
            i = randint(0, len(self.array) - 1)
            j = i
            while j == i:
                j = randint(0, len(self.array) - 1)
            moves.append(NumberCardOperations.create_compare_operation(i, j))
            moves.append(NumberCardOperations.create_swap_operation(i, j))
            current[i], current[j] = current[j], current[i]

        return moves
