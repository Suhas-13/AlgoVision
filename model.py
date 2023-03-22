from constants import *
import pygame

class Model:
    def __init__(self, controller):
        self.controller = controller

    def next_question(self):
        self.controller.questionNumber += 1
        self.controller.answers = []
        self.controller.surfaces = []
        self.controller.questions = []

        self.controller.view.init_answers()
        self.controller.view.init_question()



    def update(self):
        #what happens after user selects answer, correct or incorrect
        pass