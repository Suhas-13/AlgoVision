from constants import *
from controller import *
import pygame
import json
import random
pygame.init()

class Text:
    def __init__(self,text,x,y,size,draw_background, rect_color, rect_size):
        self.text = text
        self.font = pygame.font.SysFont("Arial",size)
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

    def draw(self, screen):
        screen.blit(self.background_surface, (self.x, self.y))


class AnswerButton(Text):
    def __init__(self, text, x, y, size, correct, draw_background=True, rect_color=LIGHT_GREY, rect_size=(ANSWER_LENGTH,ANSWER_HEIGHT), highlighted=False):
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
    def __init__(self, x, y, height, width, text, rect_color=LIGHT_GREY, size=30, draw_background=False, rect_size=(100,1100)):
        Text.__init__(self, text, x, y, 30, draw_background, rect_color, rect_size)
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.size = size
        self.rect_color = rect_color
    
class PointsBox(Text):
    def __init__(self, text, height = 100, width = 100, x = 50, y = 50, rect_color=None, size=30, draw_background=False, rect_size=(200,200)):
        Text.__init__(self, text, x, y, 30, draw_background, rect_color, rect_size)
        self.text = text

class EndScreen(Text):
    def __init__(self, text, height = 500, width = 500, x = 400, y = 0, rect_color=None, size=30, draw_background=False, rect_size=(500,500)):
        Text.__init__(self, text, x, y, 30, draw_background, rect_color, rect_size)

class View:
    def __init__(self,controller):
        self.controller = controller
        self.canvas = pygame.display.set_mode((CANVAS_WIDTH, CANVAS_HEIGHT))
        self.canvas.fill(WHITE)
        pygame.display.set_caption("AlgoVision")

        self.init_answers()
        self.init_question()
        self.init_points()

    def endScreen(self):
        points=self.controller.points
        text = "You got "+points+"!"
        EndScreen(text)

    def openFile(self):
        file = open("mcq.json")
        database = json.load(file)
        file.close()
        return database
    
    def correctAnsPos(self):
        x = random.randint(1,4)
        return x

    def incorrectAnsPos(self, corrPos):
        x = []
        if corrPos == 1:
            x = [True,False,False,False]
        elif corrPos == 2:
            x = [False,True,False,False]
        elif corrPos == 3:
            x = [False,False,True,False]
        elif corrPos == 4:
            x = [False,False,False,True]
        return x

    def choose_question(self):
        data = self.openFile()
        q = data[self.controller.mode][self.controller.questionNumber - 1]["question"]
        return q
    
    def determine_answers(self, corrArr):
        data = self.openFile()
        text=[0,0,0,0]
        print(corrArr)
        if corrArr[0]:
            text[0] = data[self.controller.mode][self.controller.questionNumber - 1]["right"]
            text[1] = data[self.controller.mode][self.controller.questionNumber - 1]["wrong3"]
            text[2] = data[self.controller.mode][self.controller.questionNumber - 1]["wrong1"]
            text[3] = data[self.controller.mode][self.controller.questionNumber - 1]["wrong2"]
        elif corrArr[1]:
            text[0] = data[self.controller.mode][self.controller.questionNumber - 1]["wrong2"]
            text[1] = data[self.controller.mode][self.controller.questionNumber - 1]["right"]
            text[2] = data[self.controller.mode][self.controller.questionNumber - 1]["wrong1"]
            text[3] = data[self.controller.mode][self.controller.questionNumber - 1]["wrong3"]
        elif corrArr[2]:
            text[0] = data[self.controller.mode][self.controller.questionNumber - 1]["wrong1"]
            text[1] = data[self.controller.mode][self.controller.questionNumber - 1]["wrong2"]
            text[2] = data[self.controller.mode][self.controller.questionNumber - 1]["right"]
            text[3] = data[self.controller.mode][self.controller.questionNumber - 1]["wrong3"]
        elif corrArr[3]:
            text[0] = data[self.controller.mode][self.controller.questionNumber - 1]["wrong1"]
            text[1] = data[self.controller.mode][self.controller.questionNumber - 1]["wrong2"]
            text[2] = data[self.controller.mode][self.controller.questionNumber - 1]["wrong3"]
            text[3] = data[self.controller.mode][self.controller.questionNumber - 1]["right"]

        return text
    

    def init_question(self):
        text=self.choose_question()
        self.controller.register_question_box(QuestionBox(QUESTION_X,QUESTION_Y,100,1100,text))

    def init_answers(self):
        yCounter=0
        corrPos = self.correctAnsPos()
        isCorrect = self.incorrectAnsPos(corrPos)
        textArr = self.determine_answers(isCorrect)
        for i in range(4):
            self.controller.register_answer_boxes(
                AnswerButton(textArr[i-1], ANSWER_X, ANSWER_Y+yCounter, 25, isCorrect[i-1])
            )
            yCounter+=100

    def init_points(self):
        print("in pts")
        points = self.controller.points
        text = "Points: "+points
        PointsBox(text)

    def update(self):
        self.canvas.fill(WHITE)
