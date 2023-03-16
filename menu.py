import sys
import pygame
import json
import random
import string

pygame.init()

width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Main Menu")

BLACK = (0, 0, 0)
GREY = pygame.Color("#D3D3D3")
BLUE = (106, 159, 181)
WHITE = (255, 255, 255)

def main_menu():
    button_width = 300
    button_height = 80
    button_spacing = 40
    border_width = 2

    total_height = button_height * 3 + button_spacing * 2

    y_offset = (height - total_height) / 2 + button_height + button_spacing - 30

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if student_button.collidepoint(pos):
                    mcq_menu()
                elif teacher_button.collidepoint(pos):
                    teacher_mode()

        screen.fill(BLUE)

        font = pygame.font.SysFont('Courier', 40)
        title_text = font.render("Main Menu", True, WHITE)
        title_rect = title_text.get_rect(center=(width/2, height/4))
        screen.blit(title_text, title_rect)

        pygame.draw.ellipse(screen, WHITE, ((width - button_width) / 2 - border_width, y_offset + 0 * (button_height + button_spacing) - border_width, button_width + 2 * border_width, button_height + 2 * border_width), border_width)
        student_button = pygame.draw.ellipse(screen, BLUE, ((width - button_width) / 2, y_offset + 0 * (button_height + button_spacing), button_width, button_height))

        font = pygame.font.SysFont('Courier', 30)
        student_text = font.render("Student Mode", True, WHITE)
        student_rect = student_text.get_rect(center=student_button.center)
        screen.blit(student_text, student_rect)

        pygame.draw.ellipse(screen, WHITE, ((width - button_width) / 2 - border_width, y_offset + 1 * (button_height + button_spacing) - border_width, button_width + 2 * border_width, button_height + 2 * border_width), border_width)
        teacher_button = pygame.draw.ellipse(screen, BLUE, ((width - button_width) / 2, y_offset + 1 * (button_height + button_spacing), button_width, button_height))
        teacher_text = font.render("Teacher Mode", True, WHITE)
        teacher_rect = teacher_text.get_rect(center=teacher_button.center)
        screen.blit(teacher_text, teacher_rect)

        pygame.display.update()


def student_mode():
    button_width = 300
    button_height = 80
    button_spacing = 40
    border_width = 2

    total_height = button_height * 3 + button_spacing * 2

    y_offset = (height - total_height) / 2 + 40

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if b_button.collidepoint(pos):
                    beginner()
                elif i_button.collidepoint(pos):
                    intermediate()
                elif a_button.collidepoint(pos):
                    advanced()

        screen.fill(BLUE)
        font = pygame.font.SysFont('Courier', 40)
        title_text = font.render("Visualisations", True, WHITE)
        title_rect = title_text.get_rect(center=(width/2, height/4 - 20))
        screen.blit(title_text, title_rect)

        b_button = pygame.draw.ellipse(screen, WHITE, ((width - button_width) / 2 - border_width, y_offset + 0 * (button_height + button_spacing) - border_width, button_width + 2 * border_width, button_height + 2 * border_width), border_width)
        b_button_inner = pygame.draw.ellipse(screen, BLUE, ((width - button_width) / 2 + border_width, y_offset + 0 * (button_height + button_spacing) + border_width, button_width - 2 * border_width, button_height - 2 * border_width))
        font = pygame.font.SysFont('Courier', 30)
        b_text = font.render("Beginner", True, WHITE)
        b_rect = b_text.get_rect(center=b_button_inner.center)
        screen.blit(b_text, b_rect)

        i_button = pygame.draw.ellipse(screen, WHITE, ((width - button_width) / 2 - border_width, y_offset + 1 * (button_height + button_spacing) - border_width, button_width + 2 * border_width, button_height + 2 * border_width), border_width)
        i_button_inner = pygame.draw.ellipse(screen, BLUE, ((width - button_width) / 2 + border_width, y_offset + 1 * (button_height + button_spacing) + border_width, button_width - 2 * border_width, button_height - 2 * border_width))
        i_text = font.render("Intermediate", True, WHITE)
        i_rect = i_text.get_rect(center=i_button_inner.center)
        screen.blit(i_text, i_rect)

        a_button = pygame.draw.ellipse(screen, WHITE, ((width - button_width) / 2 - border_width, y_offset + 2 * (button_height + button_spacing) - border_width, button_width + 2 * border_width, button_height + 2 * border_width), border_width)
        a_button_inner = pygame.draw.ellipse(screen, BLUE, ((width - button_width) / 2 + border_width, y_offset + 2 * (button_height + button_spacing) + border_width, button_width - 2 * border_width, button_height - 2 * border_width))
        a_text = font.render("Advanced", True, WHITE)
        a_rect = a_text.get_rect(center=a_button_inner.center)
        screen.blit(a_text, a_rect)

        pygame.display.update()

def mcq_menu():
    button_width = 300
    button_height = 80
    button_spacing = 40
    border_width = 2

    total_height = button_height * 3 + button_spacing * 2
    y_offset = (height - total_height) / 2 + button_height + button_spacing - 30

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if visual_button.collidepoint(pos):
                    student_mode()
                elif mcq_button.collidepoint(pos):
                    mcq()


        screen.fill(BLUE)
        font = pygame.font.SysFont('Courier', 40)
        title_text = font.render("Student Mode", True, WHITE)
        title_rect = title_text.get_rect(center=(width/2, height/4))
        screen.blit(title_text, title_rect)

        pygame.draw.ellipse(screen, WHITE, ((width - button_width) / 2 - border_width, y_offset + 0 * (button_height + button_spacing) - border_width, button_width + 2 * border_width, button_height + 2 * border_width), border_width)
        visual_button = pygame.draw.ellipse(screen, BLUE, ((width - button_width) / 2, y_offset + 0 * (button_height + button_spacing), button_width, button_height))
        font = pygame.font.SysFont('Courier', 30)
        visual_text = font.render("Visualisations", True, WHITE)
        visual_rect = visual_text.get_rect(center=visual_button.center)
        screen.blit(visual_text, visual_rect)

        pygame.draw.ellipse(screen, WHITE, ((width - button_width) / 2 - border_width, y_offset + 1 * (button_height + button_spacing) - border_width, button_width + 2 * border_width, button_height + 2 * border_width), border_width)
        mcq_button = pygame.draw.ellipse(screen, BLUE, ((width - button_width) / 2, y_offset + 1 * (button_height + button_spacing), button_width, button_height))
        mcq_text = font.render("Questions", True, WHITE)
        mcq_rect = mcq_text.get_rect(center=mcq_button.center)
        screen.blit(mcq_text, mcq_rect)

        pygame.display.update()

def beginner():
    button_width = 300
    button_height = 80
    button_spacing = 40

    total_height = button_height * 3 + button_spacing * 2 


    y_offset = (height - total_height) / 2 + 30

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if sort1_button.collidepoint(pos):
                    bsort1_page()
                elif sort2_button.collidepoint(pos):
                    bsort2_page()
                elif sort3_button.collidepoint(pos):
                    bsort3_page()

        screen.fill(BLUE)

        font = pygame.font.SysFont('Courier', 40)
        title_text = font.render("Beginner", True, WHITE)
        title_rect = title_text.get_rect(center=(width/2, height/4-40))
        screen.blit(title_text, title_rect)

        sort1_button = pygame.draw.ellipse(screen, WHITE, ((width - button_width) / 2, y_offset + 0 * (button_height + button_spacing), button_width, button_height), 2)
        font = pygame.font.SysFont('Courier', 30)
        sort1_text = font.render("B Sort 1", True, WHITE)
        sort1_rect = sort1_text.get_rect(center=sort1_button.center)
        screen.blit(sort1_text, sort1_rect)

        sort2_button = pygame.draw.ellipse(screen, WHITE, ((width - button_width) / 2, y_offset + 1 * (button_height + button_spacing), button_width, button_height), 2)
        sort2_text = font.render("B Sort 2", True, WHITE)
        sort2_rect = sort2_text.get_rect(center=sort2_button.center)
        screen.blit(sort2_text, sort2_rect)

        sort3_button = pygame.draw.ellipse(screen, WHITE, ((width - button_width) / 2, y_offset + 2 * (button_height + button_spacing), button_width, button_height), 2)
        sort3_text = font.render("B Sort 3", True, WHITE)
        sort3_rect = sort3_text.get_rect(center=sort3_button.center)
        screen.blit(sort3_text, sort3_rect)

        pygame.display.update()

def intermediate():
    button_width = 300
    button_height = 80
    button_spacing = 40

    total_height = button_height * 3 + button_spacing * 2 


    y_offset = (height - total_height) / 2 + 30

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if sort1_button.collidepoint(pos):
                    isort1_page()
                elif sort2_button.collidepoint(pos):
                    isort2_page()
                elif sort3_button.collidepoint(pos):
                    isort3_page()

        screen.fill(BLUE)
        font = pygame.font.SysFont('Courier', 40)
        title_text = font.render("Intermediate", True, WHITE)
        title_rect = title_text.get_rect(center=(width/2, height/4-40))
        screen.blit(title_text, title_rect)

        sort1_button = pygame.draw.ellipse(screen, WHITE, ((width - button_width) / 2, y_offset + 0 * (button_height + button_spacing), button_width, button_height), 2)
        font = pygame.font.SysFont('Courier', 30)
        sort1_text = font.render("I Sort 1", True, WHITE)
        sort1_rect = sort1_text.get_rect(center=sort1_button.center)
        screen.blit(sort1_text, sort1_rect)

        sort2_button = pygame.draw.ellipse(screen, WHITE, ((width - button_width) / 2, y_offset + 1 * (button_height + button_spacing), button_width, button_height), 2)
        sort2_text = font.render("I Sort 2", True, WHITE)
        sort2_rect = sort2_text.get_rect(center=sort2_button.center)
        screen.blit(sort2_text, sort2_rect)

        sort3_button = pygame.draw.ellipse(screen, WHITE, ((width - button_width) / 2, y_offset + 2 * (button_height + button_spacing), button_width, button_height), 2)
        sort3_text = font.render("I Sort 3", True, WHITE)
        sort3_rect = sort3_text.get_rect(center=sort3_button.center)
        screen.blit(sort3_text, sort3_rect)

        pygame.display.update()

def advanced():
    button_width = 300
    button_height = 80
    button_spacing = 40

    total_height = button_height * 3 + button_spacing * 2

    y_offset = (height - total_height) / 2 + 30

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if sort1_button.collidepoint(pos):
                    asort1_page()
                elif sort2_button.collidepoint(pos):
                    asort2_page()
                elif sort3_button.collidepoint(pos):
                    asort3_page()


        screen.fill(BLUE)
        font = pygame.font.SysFont('Courier', 40)
        title_text = font.render("Advanced", True, WHITE)
        title_rect = title_text.get_rect(center=(width/2, height/4-40))
        screen.blit(title_text, title_rect)

        sort1_button = pygame.draw.ellipse(screen, WHITE, ((width - button_width) / 2, y_offset + 0 * (button_height + button_spacing), button_width, button_height), 2)
        font = pygame.font.SysFont('Courier', 30)
        sort1_text = font.render("A Sort 1", True, WHITE)
        sort1_rect = sort1_text.get_rect(center=sort1_button.center)
        screen.blit(sort1_text, sort1_rect)

        sort2_button = pygame.draw.ellipse(screen, WHITE, ((width - button_width) / 2, y_offset + 1 * (button_height + button_spacing), button_width, button_height), 2)
        sort2_text = font.render("A Sort 2", True, WHITE)
        sort2_rect = sort2_text.get_rect(center=sort2_button.center)
        screen.blit(sort2_text, sort2_rect)

        sort3_button = pygame.draw.ellipse(screen, WHITE, ((width - button_width) / 2, y_offset + 2 * (button_height + button_spacing), button_width, button_height), 2)
        sort3_text = font.render("A Sort 3", True, WHITE)
        sort3_rect = sort3_text.get_rect(center=sort3_button.center)
        screen.blit(sort3_text, sort3_rect)

        pygame.display.update()
    
def teacher_mode():
    button_width = 300
    button_height = 80
    button_spacing = 40
    border_width = 2

    total_height = button_height * 3 + button_spacing * 2

    y_offset = (height - total_height) / 2 + button_height + button_spacing - 30

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if login_button.collidepoint(pos):
                    login()
                elif signup_button.collidepoint(pos):
                    signup()

        screen.fill(BLUE)

        font = pygame.font.SysFont('Courier', 40)
        title_text = font.render("Teacher Mode", True, WHITE)
        title_rect = title_text.get_rect(center=(width/2, height/4))
        screen.blit(title_text, title_rect)

        pygame.draw.ellipse(screen, WHITE, ((width - button_width) / 2 - border_width, y_offset + 0 * (button_height + button_spacing) - border_width, button_width + 2 * border_width, button_height + 2 * border_width), border_width)
        login_button = pygame.draw.ellipse(screen, BLUE, ((width - button_width) / 2, y_offset + 0 * (button_height + button_spacing), button_width, button_height))
        font = pygame.font.SysFont('Courier', 30)
        login_text = font.render("Login", True, WHITE)
        login_rect = login_text.get_rect(center=login_button.center)
        screen.blit(login_text, login_rect)

        pygame.draw.ellipse(screen, WHITE, ((width - button_width) / 2 - border_width, y_offset + 1 * (button_height + button_spacing) - border_width, button_width + 2 * border_width, button_height + 2 * border_width), border_width)
        signup_button = pygame.draw.ellipse(screen, BLUE, ((width - button_width) / 2, y_offset + 1 * (button_height + button_spacing), button_width, button_height))
        signup_text = font.render("Signup", True, WHITE)
        signup_rect = signup_text.get_rect(center=signup_button.center)
        screen.blit(signup_text, signup_rect)

        pygame.display.update()

def login():
    font = pygame.font.SysFont('Courier', 30)

    with open('teachers.json', 'r') as file:
        data = json.load(file)

    name = ''
    code = ''
    name_input = False
    code_input = False


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if not name_input:
                        name_input = True
                        print(f"Name: {name}")
                    elif not code_input:
                        code_input = True
                        print(f"Code: {code}")
                elif event.key == pygame.K_BACKSPACE:
                    if not code_input and len(name) > 0:
                        name = name[:-1]
                    elif code_input and len(code) > 0:
                        code = code[:-1]
                else:
                    if not name_input:
                        name += event.unicode
                    elif not code_input:
                        code += event.unicode

        screen.fill(BLUE)

        if not name_input:
            text = font.render('Enter your name: ' + name, True, WHITE)
        elif not code_input:
            text = font.render('Enter your code: ' + code, True, WHITE)
        else:
            data_exists = False
            for item in data['teachers']:
                if item['name'] == name and item['classroom_code'] == code:
                    data_exists = True
                    break
            if data_exists:
                text = font.render('Logged in', True, WHITE)
                running = False
            else:
                text = font.render('Incorrect name or code.', True, WHITE) #needs to allow user to login again


        
        text_rect = text.get_rect(center=(width/2, height/2))
        screen.blit(text, text_rect)
        pygame.display.update()
        

def signup():
    font = pygame.font.SysFont('Courier', 30)

    with open('teachers.json', 'r') as file:
        data = json.load(file)

    name = ''
    code = ''
    name_input = False
    code_input = False

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if not name_input:
                        name_input = True
                        print(f"Name: {name}")
                else:
                    if not name_input:
                        name += event.unicode

        screen.fill(BLUE)

        if not name_input:
            text = font.render('Enter your name: ' + name, True, WHITE)
        else:
            data_exists = True
            while data_exists == True:
                code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
                print(code)
                for item in data['teachers']:
                    if item['classroom_code'] == code:
                        data_exists = True
                    else:
                        data_exists = False
                        text = font.render('Your classroom code is ' + code, True, WHITE) #needs to show up
                        running = False

                        
            data['teachers'].append({'name': name, 'classroom_code': code})
            with open('teachers.json', 'w') as file:
                json.dump(data, file)

        
        
        text_rect = text.get_rect(center=(width/2, height/2))
        screen.blit(text, text_rect)
        pygame.display.update()

def bsort1_page():
    # Add code for beginner Sort 1 page here
    pass

def bsort2_page():
    # Add code for beginner Sort 2 page here
    pass

def bsort3_page():
    # Add code for beginner Sort 3 page here
    pass

def isort1_page():
    # Add code for intermediate Sort 1 page here
    pass

def isort2_page():
    # Add code for intermediate Sort 2 page here
    pass

def isort3_page():
    # Add code for intermediate Sort 3 page here
    pass

def asort1_page():
    # Add code for advanced Sort 1 page here
    pass

def asort2_page():
    # Add code for advanced Sort 2 page here
    pass

def asort3_page():
    # Add code for advanced Sort 3 page here
    pass

def mcq():
    pass

main_menu()

