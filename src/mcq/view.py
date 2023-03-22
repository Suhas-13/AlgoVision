from .constants import *
from .controller import *
# from user import *
import pygame
import json
import random

pygame.init()


class Text:
    def __init__(self, text, x, y, size, draw_background, rect_color, rect_size):
        self.text = text
        self.font = pygame.font.SysFont("Arial", size)
        self.x = x
        self.y = y
        self.size = size
        self.draw_background = draw_background
        self.rect_color = rect_color
        self.rect_size = rect_size

        self.update(text)

        if self.draw_background:
            self.background_surface = pygame.Surface(self.rect_size)
            self.background_surface.fill(self.rect_color)
            self.background_surface.blit(self.text_surface,
                                         ((self.background_surface.get_width() - self.text_rect.width) // 2,
                                          (self.background_surface.get_height() - self.text_rect.height) // 2))
        else:
            self.background_surface = self.text_surface

        self.rect = self.background_surface.get_rect()
        self.rect.topleft = (self.x, self.y)

    def update(self, text):
        self.text = text
        self.text_surface = self.font.render(self.text, True, BLACK)
        self.text_rect = self.text_surface.get_rect()
        self.background_surface = self.text_surface

    def draw(self, screen):
        screen.blit(self.background_surface, (self.x, self.y))


class AnswerButton(Text):
    def __init__(self, text, x, y, size, correct, draw_background=True, rect_color=LIGHT_GREY,
                 rect_size=(ANSWER_LENGTH, ANSWER_HEIGHT), highlighted=False):
        Text.__init__(self, text, x, y, size, draw_background, rect_color, rect_size)

        self.clicked = False
        self.correct = correct

    def check_mouseClick(self):
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                self.clicked = True
                if self.correct:
                    self.correctAnswer()
                elif not self.correct:
                    self.incorrectAnswer()
                return True

        if pygame.mouse.get_pressed()[0] is False:
            self.clicked = False

    def correctAnswer(self):
        self.border = pygame.Surface(
            (self.rect_size[0] + 10, self.rect_size[1] + 10))
        self.border.fill(GREEN)
        self.border.blit(self.background_surface, (1, 1))
        self.background_surface = self.border

    def incorrectAnswer(self):
        self.border = pygame.Surface(
            (self.rect_size[0] + 10, self.rect_size[1] + 10))
        self.border.fill(RED)
        self.border.blit(self.background_surface, (1, 1))
        self.background_surface = self.border


class QuestionBox(Text):
    def __init__(self, x, y, height, width, text, rect_color=LIGHT_GREY, size=30, draw_background=False,
                 rect_size=(100, 1100)):
        Text.__init__(self, text, x, y, 30, draw_background, rect_color, rect_size)
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.size = size
        self.rect_color = rect_color


class PointsBox(Text):
    def __init__(self, text, height=100, width=100, x=50, y=50, rect_color=None, size=30, draw_background=False,
                 rect_size=(200, 200)):
        Text.__init__(self, text, x, y, 30, draw_background, rect_color, rect_size)
        self.text = text


class View:
    def __init__(self, controller):
        self.controller = controller
        self.canvas = pygame.display.set_mode((CANVAS_WIDTH, CANVAS_HEIGHT))
        self.canvas.fill(WHITE)
        pygame.display.set_caption("AlgoVision")

        self.init_answers()
        self.init_question()
        self.init_points()

    def init_question(self):
        text = self.choose_question()
        self.controller.register_question_box(QuestionBox(QUESTION_X, QUESTION_Y, 100, 1100, text))

    def init_answers(self):
        yCounter = 0
        randon_list = random.sample(range(4), 4)
        print(randon_list)
        for i in randon_list:
            text, correct = self.choose_answer(i)
            self.controller.register_answer_boxes(
                AnswerButton(text, ANSWER_X, ANSWER_Y + yCounter, 25, correct)
            )
            yCounter += 100

    def choose_question(self):
        data = self.controller.database
        q = data[self.controller.mode][self.controller.questionNumber - 1]["question"]
        return q

    def choose_answer(self, n):
        data = self.controller.database
        if n == 0:
            a = data[self.controller.mode][self.controller.questionNumber - 1]["right"]
            correct = True
        if n == 1:
            a = data[self.controller.mode][self.controller.questionNumber - 1]["wrong1"]
            correct = False
        if n == 2:
            a = data[self.controller.mode][self.controller.questionNumber - 1]["wrong2"]
            correct = False
        if n == 3:
            a = data[self.controller.mode][self.controller.questionNumber - 1]["wrong3"]
            correct = False
        return a, correct

    def init_points(self):
        print("in pts")
        points = self.controller.points
        self.controller.point_box = PointsBox(f"Point: {points}")

    def update(self):
        self.canvas.fill(WHITE)
