import sys
import pygame
import json
import random
import string

# Importing custom classes
from src.animation.controller import Controller as AnimationController
from src.animation.enums import Algorithm
from src.mcq.controller import Controller as MCQController

pygame.init()

# Set screen dimensions and create screen
width = 1200
height = 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Main Menu")

# Define colour constants
BLUE = (106, 159, 181)
WHITE = (255, 255, 255)


def main_menu():
    # Define button and border dimensions and spacing
    button_width = 300
    button_height = 80
    button_spacing = 40
    border_width = 2
    # Calculate total height of buttons and spacing
    total_height = button_height * 3 + button_spacing * 2
    # Calculate y-offset to center the buttons on the screen
    y_offset = (height - total_height) / 2 + button_height + button_spacing - 30

    while True:
        # Event loop for handling quit and button clicks
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Check for mouse button click events
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Get the mouse position on click and check if it collides with a button
                pos = pygame.mouse.get_pos()
                if student_button.collidepoint(pos):
                    mcq_menu()
                elif teacher_button.collidepoint(pos):
                    teacher_mode()
                    
        # Make background blue
        screen.fill(BLUE)
        
        # Display the title
        font = pygame.font.SysFont('Courier', 40)
        title_text = font.render("AlgoVision", True, WHITE)
        title_rect = title_text.get_rect(center=(width / 2, height / 4))
        screen.blit(title_text, title_rect)

        # Draw student border with white ellipse border and blue button
        pygame.draw.ellipse(screen, WHITE, (
        (width - button_width) / 2 - border_width, y_offset + 0 * (button_height + button_spacing) - border_width,
        button_width + 2 * border_width, button_height + 2 * border_width), border_width)
        student_button = pygame.draw.ellipse(screen, BLUE, (
        (width - button_width) / 2, y_offset + 0 * (button_height + button_spacing), button_width, button_height))
        # Display student button 
        font = pygame.font.SysFont('Courier', 30)
        student_text = font.render("Student Mode", True, WHITE)
        student_rect = student_text.get_rect(center=student_button.center)
        screen.blit(student_text, student_rect)

        # Draw teacher button with white ellipse border and blue button
        pygame.draw.ellipse(screen, WHITE, (
        (width - button_width) / 2 - border_width, y_offset + 1 * (button_height + button_spacing) - border_width,
        button_width + 2 * border_width, button_height + 2 * border_width), border_width)
        teacher_button = pygame.draw.ellipse(screen, BLUE, (
        (width - button_width) / 2, y_offset + 1 * (button_height + button_spacing), button_width, button_height))
        # Display teacher button
        teacher_text = font.render("Teacher Mode", True, WHITE)
        teacher_rect = teacher_text.get_rect(center=teacher_button.center)
        screen.blit(teacher_text, teacher_rect)

        #Update screen
        pygame.display.update()

def student_mode():
    # Define button and border dimensions and spacing
    button_width = 300
    button_height = 80
    button_spacing = 40
    border_width = 2
    # Calculate total height of buttons and spacing
    total_height = button_height * 3 + button_spacing * 2
    # Calculate y-offset to center the buttons on the screen
    y_offset = (height - total_height) / 2 + 40
    # Creating the back button with a triangle shape using a transparent surface
    back_button = pygame.Surface((30, 30), pygame.SRCALPHA)
    pygame.draw.polygon(back_button, WHITE, [(15, 5), (5, 15), (15, 25)], 2)

    while True:
        # Event loop for handling quit and button clicks
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Get the mouse position on click and check if it collides with a button
                pos = pygame.mouse.get_pos()
                if b_button.collidepoint(pos):
                    beginner()
                elif i_button.collidepoint(pos):
                    intermediate()
                elif a_button.collidepoint(pos):
                    advanced()
                elif back_button.get_rect(topleft=(10, 10)).collidepoint(pos):
                    mcq_menu()

        screen.fill(BLUE)
        # Display title in the centre
        font = pygame.font.SysFont('Courier', 40)
        title_text = font.render("Visualisations", True, WHITE)
        title_rect = title_text.get_rect(center=(width / 2, height / 4 - 20))
        screen.blit(title_text, title_rect)

        # Display begineer, intermediate and advanced buttons
        b_button = pygame.draw.ellipse(screen, WHITE, (
        (width - button_width) / 2 - border_width, y_offset + 0 * (button_height + button_spacing) - border_width,
        button_width + 2 * border_width, button_height + 2 * border_width), border_width)
        b_button_inner = pygame.draw.ellipse(screen, BLUE, (
        (width - button_width) / 2 + border_width, y_offset + 0 * (button_height + button_spacing) + border_width,
        button_width - 2 * border_width, button_height - 2 * border_width))
        font = pygame.font.SysFont('Courier', 30)
        b_text = font.render("Beginner", True, WHITE)
        b_rect = b_text.get_rect(center=b_button_inner.center)
        screen.blit(b_text, b_rect)

        i_button = pygame.draw.ellipse(screen, WHITE, (
        (width - button_width) / 2 - border_width, y_offset + 1 * (button_height + button_spacing) - border_width,
        button_width + 2 * border_width, button_height + 2 * border_width), border_width)
        i_button_inner = pygame.draw.ellipse(screen, BLUE, (
        (width - button_width) / 2 + border_width, y_offset + 1 * (button_height + button_spacing) + border_width,
        button_width - 2 * border_width, button_height - 2 * border_width))
        i_text = font.render("Intermediate", True, WHITE)
        i_rect = i_text.get_rect(center=i_button_inner.center)
        screen.blit(i_text, i_rect)

        a_button = pygame.draw.ellipse(screen, WHITE, (
        (width - button_width) / 2 - border_width, y_offset + 2 * (button_height + button_spacing) - border_width,
        button_width + 2 * border_width, button_height + 2 * border_width), border_width)
        a_button_inner = pygame.draw.ellipse(screen, BLUE, (
        (width - button_width) / 2 + border_width, y_offset + 2 * (button_height + button_spacing) + border_width,
        button_width - 2 * border_width, button_height - 2 * border_width))
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
    back_button = pygame.Surface((30, 30), pygame.SRCALPHA)
    pygame.draw.polygon(back_button, WHITE, [(15, 5), (5, 15), (15, 25)], 2)

    while True:
        # Event loop for handling quit and button clicks
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
                elif back_button.get_rect(topleft=(10, 10)).collidepoint(pos):
                    main_menu()

        screen.fill(BLUE)
        font = pygame.font.SysFont('Courier', 40)
        title_text = font.render("Student Mode", True, WHITE)
        title_rect = title_text.get_rect(center=(width / 2, height / 4))
        screen.blit(title_text, title_rect)

        # Draw the back button in the top left corner
        screen.blit(back_button, (10, 10))
        
        # Display visualitsations and questions buttons
        pygame.draw.ellipse(screen, WHITE, (
        (width - button_width) / 2 - border_width, y_offset + 0 * (button_height + button_spacing) - border_width,
        button_width + 2 * border_width, button_height + 2 * border_width), border_width)
        visual_button = pygame.draw.ellipse(screen, BLUE, (
        (width - button_width) / 2, y_offset + 0 * (button_height + button_spacing), button_width, button_height))
        font = pygame.font.SysFont('Courier', 30)
        visual_text = font.render("Visualisations", True, WHITE)
        visual_rect = visual_text.get_rect(center=visual_button.center)
        screen.blit(visual_text, visual_rect)

        pygame.draw.ellipse(screen, WHITE, (
        (width - button_width) / 2 - border_width, y_offset + 1 * (button_height + button_spacing) - border_width,
        button_width + 2 * border_width, button_height + 2 * border_width), border_width)
        mcq_button = pygame.draw.ellipse(screen, BLUE, (
        (width - button_width) / 2, y_offset + 1 * (button_height + button_spacing), button_width, button_height))
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
    back_button = pygame.Surface((30, 30), pygame.SRCALPHA)
    pygame.draw.polygon(back_button, WHITE, [(15, 5), (5, 15), (15, 25)], 2)

    while True:
        # Event loop for handling quit and button clicks
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
                elif back_button.get_rect(topleft=(10, 10)).collidepoint(pos):
                    student_mode()

        screen.fill(BLUE)

        font = pygame.font.SysFont('Courier', 40)
        title_text = font.render("Beginner", True, WHITE)
        title_rect = title_text.get_rect(center=(width / 2, height / 4 - 40))
        screen.blit(title_text, title_rect)

        screen.blit(back_button, (10, 10))
        
        # Display sorting buttons
        sort1_button = pygame.draw.ellipse(screen, WHITE, (
        (width - button_width) / 2, y_offset + 0 * (button_height + button_spacing), button_width, button_height), 2)
        font = pygame.font.SysFont('Courier', 30)
        sort1_text = font.render("Bubble Sort", True, WHITE)
        sort1_rect = sort1_text.get_rect(center=sort1_button.center)
        screen.blit(sort1_text, sort1_rect)

        sort2_button = pygame.draw.ellipse(screen, WHITE, (
        (width - button_width) / 2, y_offset + 1 * (button_height + button_spacing), button_width, button_height), 2)
        sort2_text = font.render("Selection Sort", True, WHITE)
        sort2_rect = sort2_text.get_rect(center=sort2_button.center)
        screen.blit(sort2_text, sort2_rect)

        sort3_button = pygame.draw.ellipse(screen, WHITE, (
        (width - button_width) / 2, y_offset + 2 * (button_height + button_spacing), button_width, button_height), 2)
        sort3_text = font.render("Counting Sort", True, WHITE)
        sort3_rect = sort3_text.get_rect(center=sort3_button.center)
        screen.blit(sort3_text, sort3_rect)

        pygame.display.update()


def intermediate():
    button_width = 300
    button_height = 80
    button_spacing = 40

    total_height = button_height * 3 + button_spacing * 2
    y_offset = (height - total_height) / 2 + 30
    back_button = pygame.Surface((30, 30), pygame.SRCALPHA)
    pygame.draw.polygon(back_button, WHITE, [(15, 5), (5, 15), (15, 25)], 2)

    while True:
        # Event loop for handling quit and button clicks
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
                elif back_button.get_rect(topleft=(10, 10)).collidepoint(pos):
                    student_mode()

        screen.fill(BLUE)
        font = pygame.font.SysFont('Courier', 40)
        title_text = font.render("Intermediate", True, WHITE)
        title_rect = title_text.get_rect(center=(width / 2, height / 4 - 40))
        screen.blit(title_text, title_rect)

        screen.blit(back_button, (10, 10))

        # Display sorting buttons
        sort1_button = pygame.draw.ellipse(screen, WHITE, (
        (width - button_width) / 2, y_offset + 0 * (button_height + button_spacing), button_width, button_height), 2)
        font = pygame.font.SysFont('Courier', 30)
        sort1_text = font.render("Insertion Sort", True, WHITE)
        sort1_rect = sort1_text.get_rect(center=sort1_button.center)
        screen.blit(sort1_text, sort1_rect)

        sort2_button = pygame.draw.ellipse(screen, WHITE, (
        (width - button_width) / 2, y_offset + 1 * (button_height + button_spacing), button_width, button_height), 2)
        sort2_text = font.render("Bogo Sort", True, WHITE)
        sort2_rect = sort2_text.get_rect(center=sort2_button.center)
        screen.blit(sort2_text, sort2_rect)

        sort3_button = pygame.draw.ellipse(screen, WHITE, (
        (width - button_width) / 2, y_offset + 2 * (button_height + button_spacing), button_width, button_height), 2)
        sort3_text = font.render("Pancake Sort", True, WHITE)
        sort3_rect = sort3_text.get_rect(center=sort3_button.center)
        screen.blit(sort3_text, sort3_rect)

        pygame.display.update()


def advanced():
    button_width = 300
    button_height = 80
    button_spacing = 40

    total_height = button_height * 3 + button_spacing * 2
    y_offset = (height - total_height) / 2 + 30
    back_button = pygame.Surface((30, 30), pygame.SRCALPHA)
    pygame.draw.polygon(back_button, WHITE, [(15, 5), (5, 15), (15, 25)], 2)

    while True:
        # Event loop for handling quit and button clicks
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
                elif back_button.get_rect(topleft=(10, 10)).collidepoint(pos):
                    student_mode()

        screen.fill(BLUE)
        font = pygame.font.SysFont('Courier', 40)
        title_text = font.render("Advanced", True, WHITE)
        title_rect = title_text.get_rect(center=(width / 2, height / 4 - 40))
        screen.blit(title_text, title_rect)
        screen.blit(back_button, (10, 10))
        
        # Display sorting buttons
        sort1_button = pygame.draw.ellipse(screen, WHITE, (
        (width - button_width) / 2, y_offset + 0 * (button_height + button_spacing), button_width, button_height), 2)
        font = pygame.font.SysFont('Courier', 30)
        sort1_text = font.render("Merge Sort", True, WHITE)
        sort1_rect = sort1_text.get_rect(center=sort1_button.center)
        screen.blit(sort1_text, sort1_rect)

        sort2_button = pygame.draw.ellipse(screen, WHITE, (
        (width - button_width) / 2, y_offset + 1 * (button_height + button_spacing), button_width, button_height), 2)
        sort2_text = font.render("Quick Sort", True, WHITE)
        sort2_rect = sort2_text.get_rect(center=sort2_button.center)
        screen.blit(sort2_text, sort2_rect)

        sort3_button = pygame.draw.ellipse(screen, WHITE, (
        (width - button_width) / 2, y_offset + 2 * (button_height + button_spacing), button_width, button_height), 2)
        sort3_text = font.render("Heap Sort", True, WHITE)
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
    back_button = pygame.Surface((30, 30), pygame.SRCALPHA)
    pygame.draw.polygon(back_button, WHITE, [(15, 5), (5, 15), (15, 25)], 2)

    while True:
        # Event loop for handling quit and button clicks
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
                elif back_button.get_rect(topleft=(10, 10)).collidepoint(pos):
                    main_menu()

        screen.fill(BLUE)

        font = pygame.font.SysFont('Courier', 40)
        title_text = font.render("Teacher Mode", True, WHITE)
        title_rect = title_text.get_rect(center=(width / 2, height / 4))
        screen.blit(title_text, title_rect)
        screen.blit(back_button, (10, 10))

        # Display login and sign up buttons
        pygame.draw.ellipse(screen, WHITE, (
        (width - button_width) / 2 - border_width, y_offset + 0 * (button_height + button_spacing) - border_width,
        button_width + 2 * border_width, button_height + 2 * border_width), border_width)
        login_button = pygame.draw.ellipse(screen, BLUE, (
        (width - button_width) / 2, y_offset + 0 * (button_height + button_spacing), button_width, button_height))
        font = pygame.font.SysFont('Courier', 30)
        login_text = font.render("Login", True, WHITE)
        login_rect = login_text.get_rect(center=login_button.center)
        screen.blit(login_text, login_rect)

        pygame.draw.ellipse(screen, WHITE, (
        (width - button_width) / 2 - border_width, y_offset + 1 * (button_height + button_spacing) - border_width,
        button_width + 2 * border_width, button_height + 2 * border_width), border_width)
        signup_button = pygame.draw.ellipse(screen, BLUE, (
        (width - button_width) / 2, y_offset + 1 * (button_height + button_spacing), button_width, button_height))
        signup_text = font.render("Signup", True, WHITE)
        signup_rect = signup_text.get_rect(center=signup_button.center)
        screen.blit(signup_text, signup_rect)

        pygame.display.update()


def login():
    # Set font and load teacher data from json file
    font = pygame.font.SysFont('Courier', 30)
    with open('./datas/teachers.json', 'r') as file:
        data = json.load(file)

    # Initialize name and code inputs and back button
    name = ''
    code = ''
    name_input = False
    code_input = False
    back_button = pygame.Surface((30, 30), pygame.SRCALPHA)
    pygame.draw.polygon(back_button, WHITE, [(15, 5), (5, 15), (15, 25)], 2)

    running = True
    while running:
        # Check for events
        for event in pygame.event.get():
            # Check if user quits the game
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Check if user clicks the back button
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if back_button.get_rect(topleft=(10, 10)).collidepoint(pos):
                    teacher_mode()
            # Check if user types something
            elif event.type == pygame.KEYDOWN:
                # If the user hits return, move to next input 
                if event.key == pygame.K_RETURN:
                    if not name_input:
                        name_input = True
                    elif not code_input:
                        code_input = True
                # If the user hits backspace, delete the last character entered
                elif event.key == pygame.K_BACKSPACE:
                    if not code_input and len(name) > 0:
                        name = name[:-1]
                    elif code_input and len(code) > 0:
                        code = code[:-1]
                # Otherwise, add the typed character to the input field
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
        # If name and code inputs are complete, check if data exists in JSON file
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
                text = font.render('Incorrect name or code. Press try again.', True, WHITE)
                name = ''
                code = ''
                name_input = False
                code_input = False
                text_rect = text.get_rect(center=(width / 2, height / 2))
                screen.blit(text, text_rect)
                pygame.display.update()
                # Wait for user to press a key before continuing
                waiting = True
                while waiting:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            waiting = False
                            break
                        elif event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()

        screen.blit(back_button, (10, 10))
        text_rect = text.get_rect(center=(width / 2, height / 2))
        screen.blit(text, text_rect)
        pygame.display.update()


def signup():
    # Set font and load teacher data from json file
    font = pygame.font.SysFont('Courier', 30)
    with open('./datas/teachers.json', 'r') as file:
        data = json.load(file)

    # Initialize name and code inputs and back button
    name = ''
    code = ''
    name_input = False
    back_button = pygame.Surface((30, 30), pygame.SRCALPHA)
    pygame.draw.polygon(back_button, WHITE, [(15, 5), (5, 15), (15, 25)], 2)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if back_button.get_rect(topleft=(10, 10)).collidepoint(pos):
                    teacher_mode()
            elif event.type == pygame.KEYDOWN:
                # If user presses return key, move on to code input
                if event.key == pygame.K_RETURN:
                    if not name_input:
                        name_input = True
                # If user presses backspace key, delete last character of name input
                elif event.key == pygame.K_BACKSPACE:
                    if len(name) > 0:
                        name = name[:-1]
                # If user types any other key, add the character to the name input
                else:
                    if not name_input:
                        name += event.unicode

        screen.fill(BLUE)

        if not name_input:
            text = font.render('Enter your name: ' + name, True, WHITE)
        else:
            code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
            text = font.render('Your classroom code is ' + code, True, WHITE)
            text_rect = text.get_rect(center=(width / 2, height / 2))
            screen.blit(text, text_rect)

            # Write updated teacher data to json file
            data['teachers'].append({'name': name, 'classroom_code': code})
            with open('./datas/teachers.json', 'w') as file:
                json.dump(data, file)
            running = False
            for i in range(0, 1000):
                pygame.display.update()

        screen.blit(back_button, (10, 10))
        text_rect = text.get_rect(center=(width / 2, height / 2))
        screen.blit(text, text_rect)
        pygame.display.update()


def bsort1_page():
    pygame.event.clear()
    bubble_sort = AnimationController(Algorithm.BUBBLE_SORT)
    bubble_sort.run()


def bsort2_page():
    selection_sort = AnimationController(Algorithm.SELECTION_SORT)
    selection_sort.run()


def bsort3_page():
    # Add code for beginner Sort 3 page here
    pass


def isort1_page():
    insertion_sort = AnimationController(Algorithm.INSERTION_SORT)
    insertion_sort.run()


def isort2_page():
    bogo_sort = AnimationController(Algorithm.BOGO_SORT)
    bogo_sort.run()


def isort3_page():
    # Add code for intermediate Sort 3 page here
    pass


def asort1_page():
    merge_sort = AnimationController(Algorithm.MERGE_SORT)
    merge_sort.run()


def asort2_page():
    # Add code for advanced Sort 2 page here
    pass


def asort3_page():
    # Add code for advanced Sort 3 page here
    pass


def mcq():
    MCQController(mode="bubble").run()


if __name__ == "__main__":
    main_menu()


