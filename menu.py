import sys
import pygame

pygame.init()

# Set up the screen
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Main Menu")

# Define colors
BLACK = (0, 0, 0)
GREY = pygame.Color("#D3D3D3")
BLUE = (106, 159, 181)
WHITE = (255, 255, 255)

def main_menu():
    button_width = 200
    button_height = 50
    button_spacing = 20

    # Calculate total height of buttons and spacing
    total_height = button_height * 3 + button_spacing * 2

    # Calculate y coordinate of top of buttons
    y_offset = (height - total_height) / 2 + button_height + button_spacing

    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if student_button.collidepoint(pos):
                    #student_mode()
                    mcq_menu()
                elif teacher_button.collidepoint(pos):
                    teacher_mode()

        # Clear the screen
        screen.fill(BLUE)

        # Draw title text
        font = pygame.font.SysFont('Courier', 40)
        title_text = font.render("Main Menu", True, WHITE)
        title_rect = title_text.get_rect(center=(width/2, height/4))
        screen.blit(title_text, title_rect)

        # Draw buttons
        student_button = pygame.draw.ellipse(screen, BLUE, ((width - button_width) / 2, y_offset + 0 * (button_height + button_spacing), button_width, button_height))
        font = pygame.font.SysFont('Courier', 30)
        student_text = font.render("Student Mode", True, WHITE)
        student_rect = student_text.get_rect(center=student_button.center)
        screen.blit(student_text, student_rect)

        teacher_button = pygame.draw.ellipse(screen, BLUE, ((width - button_width) / 2, y_offset + 1 * (button_height + button_spacing), button_width, button_height))
        teacher_text = font.render("Teacher Mode", True, WHITE)
        teacher_rect = teacher_text.get_rect(center=teacher_button.center)
        screen.blit(teacher_text, teacher_rect)

        # Update the screen
        pygame.display.update()

def student_mode():

    # Define button dimensions and spacing
    button_width = 200
    button_height = 50
    button_spacing = 20

    # Calculate total height of buttons and spacing
    total_height = button_height * 3 + button_spacing * 2

    # Calculate y coordinate of top of buttons
    y_offset = (height - total_height) / 2

    while True:
        # Handle events
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

        # Clear the screen
        screen.fill(BLUE)

        # Draw title text
        font = pygame.font.SysFont('Courier', 40)
        title_text = font.render("Visualisations", True, WHITE)
        title_rect = title_text.get_rect(center=(width/2, height/4))
        screen.blit(title_text, title_rect)

        # Draw buttons
        b_button = pygame.draw.ellipse(screen, BLUE, ((width - button_width) / 2, y_offset + 0 * (button_height + button_spacing), button_width, button_height))
        font = pygame.font.SysFont('Courier', 30)
        b_text = font.render("Beginner", True, WHITE)
        b_rect = b_text.get_rect(center=b_button.center)
        screen.blit(b_text, b_rect)

        i_button = pygame.draw.ellipse(screen, BLUE, ((width - button_width) / 2, y_offset + 1 * (button_height + button_spacing), button_width, button_height))
        i_text = font.render("Intermediate", True, WHITE)
        i_rect = i_text.get_rect(center=i_button.center)
        screen.blit(i_text, i_rect)

        a_button = pygame.draw.ellipse(screen, BLUE, ((width - button_width) / 2, y_offset + 2 * (button_height + button_spacing), button_width, button_height))
        a_text = font.render("Advanced", True, WHITE)
        a_rect = a_text.get_rect(center=a_button.center)
        screen.blit(a_text, a_rect)

        # Update the screen
        pygame.display.update()

def mcq_menu():
    button_width = 200
    button_height = 50
    button_spacing = 20

    total_height = button_height * 3 + button_spacing * 2
    y_offset = (height - total_height) / 2 + button_height + button_spacing

    while True:
        # Handle events
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

        # Clear the screen
        screen.fill(BLUE)

        # Draw title text
        font = pygame.font.SysFont('Courier', 40)
        title_text = font.render("Student Mode", True, WHITE)
        title_rect = title_text.get_rect(center=(width/2, height/4))
        screen.blit(title_text, title_rect)

        # Draw buttons
        visual_button = pygame.draw.ellipse(screen, BLUE, ((width - button_width) / 2, y_offset + 0 * (button_height + button_spacing), button_width, button_height))
        font = pygame.font.SysFont('Courier', 30)
        visual_text = font.render("Visualisations", True, WHITE)
        visual_rect = visual_text.get_rect(center=visual_button.center)
        screen.blit(visual_text, visual_rect)

        mcq_button = pygame.draw.ellipse(screen, BLUE, ((width - button_width) / 2, y_offset + 1 * (button_height + button_spacing), button_width, button_height))
        mcq_text = font.render("Multiple Choice Questions", True, WHITE)
        mcq_rect = mcq_text.get_rect(center=mcq_button.center)
        screen.blit(mcq_text, mcq_rect)

        # Update the screen
        pygame.display.update()

def beginner():
    button_width = 200
    button_height = 50
    button_spacing = 20

    # Calculate total height of buttons and spacing
    total_height = button_height * 3 + button_spacing * 2

    # Calculate y coordinate of top of buttons
    y_offset = (height - total_height) / 2

    while True:
        # Handle events
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

        # Clear the screen
        screen.fill(BLUE)

        # Draw title text
        font = pygame.font.SysFont('Courier', 40)
        title_text = font.render("Beginner", True, WHITE)
        title_rect = title_text.get_rect(center=(width/2, height/4))
        screen.blit(title_text, title_rect)

        # Draw buttons
        sort1_button = pygame.draw.ellipse(screen, BLUE, ((width - button_width) / 2, y_offset + 0 * (button_height + button_spacing), button_width, button_height))
        font = pygame.font.SysFont('Courier', 30)
        sort1_text = font.render("B Sort 1", True, WHITE)
        sort1_rect = sort1_text.get_rect(center=sort1_button.center)
        screen.blit(sort1_text, sort1_rect)

        sort2_button = pygame.draw.ellipse(screen, BLUE, ((width - button_width) / 2, y_offset + 1 * (button_height + button_spacing), button_width, button_height))
        sort2_text = font.render("B Sort 2", True, WHITE)
        sort2_rect = sort2_text.get_rect(center=sort2_button.center)
        screen.blit(sort2_text, sort2_rect)

        sort3_button = pygame.draw.ellipse(screen, BLUE, ((width - button_width) / 2, y_offset + 2 * (button_height + button_spacing), button_width, button_height))
        sort3_text = font.render("B Sort 3", True, WHITE)
        sort3_rect = sort3_text.get_rect(center=sort3_button.center)
        screen.blit(sort3_text, sort3_rect)

        # Update the screen
        pygame.display.update()

def intermediate():
    button_width = 200
    button_height = 50
    button_spacing = 20

    # Calculate total height of buttons and spacing
    total_height = button_height * 3 + button_spacing * 2

    # Calculate y coordinate of top of buttons
    y_offset = (height - total_height) / 2

    while True:
        # Handle events
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

        # Clear the screen
        screen.fill(BLUE)

        # Draw title text
        font = pygame.font.SysFont('Courier', 40)
        title_text = font.render("Intermediate", True, WHITE)
        title_rect = title_text.get_rect(center=(width/2, height/4))
        screen.blit(title_text, title_rect)

        # Draw buttons
        sort1_button = pygame.draw.ellipse(screen, BLUE, ((width - button_width) / 2, y_offset + 0 * (button_height + button_spacing), button_width, button_height))
        font = pygame.font.SysFont('Courier', 30)
        sort1_text = font.render("I Sort 1", True, WHITE)
        sort1_rect = sort1_text.get_rect(center=sort1_button.center)
        screen.blit(sort1_text, sort1_rect)

        sort2_button = pygame.draw.ellipse(screen, BLUE, ((width - button_width) / 2, y_offset + 1 * (button_height + button_spacing), button_width, button_height))
        sort2_text = font.render("I Sort 2", True, WHITE)
        sort2_rect = sort2_text.get_rect(center=sort2_button.center)
        screen.blit(sort2_text, sort2_rect)

        sort3_button = pygame.draw.ellipse(screen, BLUE, ((width - button_width) / 2, y_offset + 2 * (button_height + button_spacing), button_width, button_height))
        sort3_text = font.render("I Sort 3", True, WHITE)
        sort3_rect = sort3_text.get_rect(center=sort3_button.center)
        screen.blit(sort3_text, sort3_rect)

        # Update the screen
        pygame.display.update()

def advanced():
    button_width = 200
    button_height = 50
    button_spacing = 20

    # Calculate total height of buttons and spacing
    total_height = button_height * 3 + button_spacing * 2

    # Calculate y coordinate of top of buttons
    y_offset = (height - total_height) / 2

    while True:
        # Handle events
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

        # Clear the screen
        screen.fill(BLUE)

        # Draw title text
        font = pygame.font.SysFont('Courier', 40)
        title_text = font.render("Advanced", True, WHITE)
        title_rect = title_text.get_rect(center=(width/2, height/4))
        screen.blit(title_text, title_rect)

        # Draw buttons
        sort1_button = pygame.draw.ellipse(screen, BLUE, ((width - button_width) / 2, y_offset + 0 * (button_height + button_spacing), button_width, button_height))
        font = pygame.font.SysFont('Courier', 30)
        sort1_text = font.render("A Sort 1", True, WHITE)
        sort1_rect = sort1_text.get_rect(center=sort1_button.center)
        screen.blit(sort1_text, sort1_rect)

        sort2_button = pygame.draw.ellipse(screen, BLUE, ((width - button_width) / 2, y_offset + 1 * (button_height + button_spacing), button_width, button_height))
        sort2_text = font.render("A Sort 2", True, WHITE)
        sort2_rect = sort2_text.get_rect(center=sort2_button.center)
        screen.blit(sort2_text, sort2_rect)

        sort3_button = pygame.draw.ellipse(screen, BLUE, ((width - button_width) / 2, y_offset + 2 * (button_height + button_spacing), button_width, button_height))
        sort3_text = font.render("A Sort 3", True, WHITE)
        sort3_rect = sort3_text.get_rect(center=sort3_button.center)
        screen.blit(sort3_text, sort3_rect)

        # Update the screen
        pygame.display.update()
    
def teacher_mode():
    pass

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
