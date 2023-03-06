import pygame
import sys
import math

pygame.init()

# Set up the screen
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Main Menu")

# Define colors
BLACK = (0, 0, 0)
GREY = pygame.Color("#D3D3D3")
BLUE = pygame.Color("#b0e0e6")

def main_menu():
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
                if student_button.collidepoint(pos):
                    student_mode()
                elif teacher_button.collidepoint(pos):
                    teacher_mode()

        # Clear the screen
        screen.fill(BLUE)

        # Draw title text
        font = pygame.font.SysFont(None, 72)
        title_text = font.render("Main Menu", True, BLACK)
        title_rect = title_text.get_rect(center=(width/2, height/4))
        screen.blit(title_text, title_rect)

        # Draw buttons
        student_button = pygame.draw.ellipse(screen, GREY, ((width - button_width) / 2, y_offset + 0 * (button_height + button_spacing), button_width, button_height))
        font = pygame.font.SysFont(None, 30)
        student_text = font.render("Student Mode", True, BLACK)
        student_rect = student_text.get_rect(center=student_button.center)
        screen.blit(student_text, student_rect)

        teacher_button = pygame.draw.ellipse(screen, GREY, ((width - button_width) / 2, y_offset + 1 * (button_height + button_spacing), button_width, button_height))
        teacher_text = font.render("Teacher Mode", True, BLACK)
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
                if sort1_button.collidepoint(pos):
                    sort1_page()
                elif sort2_button.collidepoint(pos):
                    sort2_page()
                elif sort3_button.collidepoint(pos):
                    sort3_page()

        # Clear the screen
        screen.fill(BLUE)

        # Draw title text
        font = pygame.font.SysFont(None, 72)
        title_text = font.render("Student Mode", True, BLACK)
        title_rect = title_text.get_rect(center=(width/2, height/4))
        screen.blit(title_text, title_rect)

        # Draw buttons
        sort1_button = pygame.draw.ellipse(screen, GREY, ((width - button_width) / 2, y_offset + 0 * (button_height + button_spacing), button_width, button_height))
        font = pygame.font.SysFont(None, 48)
        sort1_text = font.render("Sort 1", True, BLACK)
        sort1_rect = sort1_text.get_rect(center=sort1_button.center)
        screen.blit(sort1_text, sort1_rect)

        sort2_button = pygame.draw.ellipse(screen, GREY, ((width - button_width) / 2, y_offset + 1 * (button_height + button_spacing), button_width, button_height))
        sort2_text = font.render("Sort 2", True, BLACK)
        sort2_rect = sort2_text.get_rect(center=sort2_button.center)
        screen.blit(sort2_text, sort2_rect)

        sort3_button = pygame.draw.ellipse(screen, GREY, ((width - button_width) / 2, y_offset + 2 * (button_height + button_spacing), button_width, button_height))
        sort3_text = font.render("Sort 3", True, BLACK)
        sort3_rect = sort3_text.get_rect(center=sort3_button.center)
        screen.blit(sort3_text, sort3_rect)

        # Update the screen
        pygame.display.update()

def teacher_mode():
    pass

def sort1_page():
    # Add code for Sort 1 page here
    pass

def sort2_page():
    # Add code for Sort 2 page here
    pass

def sort3_page():
    # Add code for Sort 3 page here
    pass

main_menu()


#its not finished yet i dont like the way it looks
