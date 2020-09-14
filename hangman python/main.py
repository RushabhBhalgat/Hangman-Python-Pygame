import pygame
import os
import math
import random
import pkg_resources.py2_warn


pygame.init()  # First Step To Initiate The Game
'''
Written In Capital Because The Values Will Be Constant And It Is 
A Good Practice To Write Constant Variables in capital letters 
'''

# Setup Window
WIDTH = 800
HEIGHT = 500
window = pygame.display.set_mode((WIDTH, HEIGHT))
caption = pygame.display.set_caption("Hangman Game!")

# Button Variable
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])

# FONTS
LETTER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 60)
TITLE_FONT = pygame.font.SysFont('comicsans', 70)


# Loading The Images
images = []
for i in range(7):
    image = pygame.image.load("images/hangman" + str(i) + ".png")
    images.append(image)

# GAME VARIABLES
hangman_status = 0
words = ["DEVELOPER", "HELLO", "MOTHER", "FATHER", "MONITOR", "FURIOUS", "GAMING", "PYTHON", "PYGAME", "DJANGO", "PROGRAMING", "CODING", "SPEAKERS", "ELEPHANT", "TOUCAN", "BEDSHEET", "PILLOW", "CHARGER", "MOBILE", "WALLET", "PENCIL", "GRAPHICS"]
word =random.choice(words)
guessed = []

# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# setup Main Loop
FPS = 60
clock = pygame.time.Clock()
run = True


# FUNCTIONS 
def Lost_Won_Message(message):
    pygame.time.delay(2000)
    window.fill(WHITE)
    text = WORD_FONT.render(message, 1, BLACK)
    window.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(5000)
    print(message)

def Draw_Letters():
    window.fill(WHITE)
    text = TITLE_FONT.render("HANGMAN IN PYGAME", 1, BLACK)
    window.blit(text, (WIDTH / 2 - text.get_width() / 2, 20))
    # Draw Word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    window.blit(text, (400, 200))

    # DRAW LETTERS
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(window, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            window.blit(text, (x - text.get_width()/2, y - text.get_height()/2))


    window.blit(images[hangman_status], (150, 100))
    pygame.display.update()



# The Main Loop
while run:
    clock.tick(FPS)
    Draw_Letters()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            for letter in letters:
                x, y, ltr, visible = letter
                if visible:
                    distance = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)
                    if distance < RADIUS:
                        letter[3] = False
                        guessed.append(ltr)
                        if ltr not in word:
                            hangman_status += 1
    won =True
    for letter in word:
        if letter not in guessed:
            won = False
            break

    if won:
        Lost_Won_Message("You WON !")
        break

    if hangman_status == 6:
        Lost_Won_Message("You LOST !!")
        break


pygame.quit()
