import pygame
import sys
import time

from model import Model
from view import *
from user import *

class Controller:
    def __init__(self, questionNumber=1, mode = "bubble", points = 0):
        self.answers = []
        self.surfaces = []
        self.questions = []
        self.questionNumber = questionNumber
        self.mode = mode
        self.points = points

        self.model = Model(self)
        self.view = View(self)

    def register_answer_boxes(self, answer):
        self.surfaces.append(answer)
        self.answers.append(answer)
    
    def register_question_box(self, question):
        self.questions.append(question)
        self.surfaces.append(question)

    def addPoint(self):
        self.points += 1

    def check_answerBox_click(self):
        for answer in self.answers:
            if answer.check_mouseClick():
                if answer.correct:
                    self.addPoint()
                    self.questionNumber += 1
                    time.sleep(3)
                if not answer.correct:
                    self.questionNumber += 1
                    time.sleep(3)
                    pass

    def check_exit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def run(self):
        while True:
            self.check_exit()
            self.check_answerBox_click()

            self.view.update()
            for surface in self.surfaces:
                surface.draw(self.view.canvas)

            

            self.model.update()
            pygame.display.update()