class Model:
    def __init__(self, controller):
        self.controller = controller

    # remove all answers and questions, and then initialize the next one
    def next_question(self):
        self.controller.questionNumber += 1
        self.controller.answers = []
        self.controller.surfaces = []
        self.controller.questions = []

        self.controller.view.init_answers()
        self.controller.view.init_question()