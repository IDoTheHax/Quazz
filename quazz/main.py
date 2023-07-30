# Quazz - a Python Quiz Game Implementing ChatGPT
# (C) - Matty Mcleod-Illert 2023

# Imports
import pygame
import button

icon_image = pygame.image.load('icon.png')

WIDTH = 850
HEIGHT = 720
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Quazz')
pygame.display.set_icon(icon_image)

# Load Images
# Load button Images
default_img = pygame.image.load('images/default.png')
incorrect_img = pygame.image.load('images/incorrect.png')
correct_img = pygame.image.load('images/correct.png')
quit_img = pygame.image.load('images/quit.png')

# Create button instances
quiz_answer1 = button.Button(100, 100, default_img, 1.5)
quiz_answer2 = button.Button(450, 100, default_img, 1.5)
quiz_answer3 = button.Button(100, 300, default_img, 1.5)
quiz_answer4 = button.Button(450, 300, default_img, 1.5)

incorrect_btn = button.Button(-100, -100, incorrect_img, 1)
correct_btn = button.Button(-100, -100, correct_img, 1)

quit_btn = button.Button(10, 10, quit_img, 0.4)

# Game loop
run = True
while run:

    screen.fill((202, 228, 241))

    # call the draw function in the button class
    if quiz_answer1.draw(screen):
        print('ANSWER 1')
    if quiz_answer2.draw(screen):
        print('ANSWER 2')
    if quiz_answer3.draw(screen):
        print('ANSWER 3')
    if quiz_answer4.draw(screen):
        print('ANSWER 4')

    if quit_btn.draw(screen):
        run = False

    incorrect_btn.draw(screen)
    correct_btn.draw(screen)

    for event in pygame.event.get():
        # Quit
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
