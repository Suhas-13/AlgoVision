from .view import *
from .model import *
import json
import sys


class Controller:
    def __init__(self, questionNumber=1, mode="bubble", points=0):
        self.database = self.openFile()
        self.init_click = True
        self.answers = []
        self.surfaces = []
        self.questions = []
        self.point_box = None

        self.questionNumber = questionNumber
        self.mode = mode
        self.points = points

        self.model = Model(self)
        self.view = View(self)

        self.answered = False

    # get all of the questions from json file
    def openFile(self):
        file = open("./datas/mcq.json", "r")
        database = json.load(file)
        file.close()
        return database

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
            if self.init_click:
                break

            # check if the answer is clicked, and the correctness of the answer
            if answer.check_mouseClick():
                if answer.correct:
                    self.addPoint()
                    answer.click = False
                    answer.correctAnswer()
                    # set self.answered to True to prepare for the next question
                    self.answered = True
                    break
                if not answer.correct:
                    answer.incorrectAnswer()
                    answer.click = False
                    self.answered = True
                    break

    def check_exit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP and self.init_click:
                self.init_click = False

    def run(self):
        while True:
            self.check_exit()
            self.check_answerBox_click()

            # update the screen
            self.view.update()
            for surface in self.surfaces:
                surface.draw(self.view.canvas)
            self.point_box.draw(self.view.canvas)
            pygame.display.update()

            # prepare for the next question
            if self.answered:
                self.answered = False
                self.point_box.update(f"Points: {self.points} / {self.questionNumber}")
                pygame.time.delay(1000)
                self.model.next_question()

                if self.questionNumber == 10:
                    return
