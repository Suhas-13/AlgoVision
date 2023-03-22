CANVAS_HEIGHT = 700
CANVAS_WIDTH = 1200

BLACK = (0, 0, 0)
LIGHT_GREY = (233, 233, 233)
GREY = (30, 30, 30)
HIGHLIGHT_COLOR = (255, 255, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (106, 159, 181)

SQUARE_SIZE = 50
GAP = 75

CARD_X_POS = [400 + SQUARE_SIZE / 2 + GAP * i for i in range(10)]
CARD_Y_POS = [150, 250, 350, 450, 550]

MERGE_SORT_X_POS = {0: [550 + SQUARE_SIZE * i for i in range(10)],
                    1: [520 + SQUARE_SIZE * i for i in range(5)] +
                       [830 + SQUARE_SIZE * i for i in range(5)],
                    2: [490 + SQUARE_SIZE * i for i in range(3)] + [700 + SQUARE_SIZE * i for i in range(2)] +
                       [800 + SQUARE_SIZE * i for i in range(3)] + [1010 + SQUARE_SIZE * i for i in range(2)],
                    3: [460 + SQUARE_SIZE * i for i in range(2)] + [620, 670, 780] +
                       [770 + SQUARE_SIZE * i for i in range(2)] + [930, 980, 1100],
                    4: [430, 540, None, None, None, 740, 850, None, None, None]}
