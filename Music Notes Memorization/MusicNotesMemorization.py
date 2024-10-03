# Kenta Festag
# Music Note Indentification Game

# Imports and init
import pygame
import random
import sys
pygame.init()

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 720
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Music Note Identification Game")

# Music notes
TrebleNotes = ["A6", "G6", "F6", "E6", "D6", "C6", "B5", "A5", "G5", "F5", "E5", "D5", "C5", "B4", "A4", "G4", "F4", "E4", "D4", "C4", "B3", "A3", "G3", "F3", "E3"]

# Game variables for adjustment
timePerNote = 2 # in seconds
mode = 1 #0 for both, 1 for treble only, 2 for bass only
numberOfNotes = 20
fontSize = 36
noteStart = 9 #For treble min 0
noteEnd = 19 #For treble max 24

# Game variables for operation
selection = []
font = pygame.font.Font(None, fontSize)
noteX = 0
noteY = 0

# Game loop
running = True
clock = pygame.time.Clock()
TIMER_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(TIMER_EVENT, 1000*timePerNote) #1000 per second
notesPassed = 0

# Loading Images
backgroundIMG = pygame.image.load("treble_base_staff.jpg")
noteIMG = pygame.image.load("quarter_note.png")
noteIMGF = pygame.transform.flip(noteIMG, True, True)

# Ledger Line Functions
def A5LL():
    pygame.draw.rect(screen, BLACK, (276, 148, 50, 6))
def C6LL():
    pygame.draw.rect(screen, BLACK, (276, 120, 50, 6))
def E6LL():
    pygame.draw.rect(screen, BLACK, (276, 92, 50, 6))
def G6LL():
    pygame.draw.rect(screen, BLACK, (276, 64, 50, 6))
def C4LL():
    pygame.draw.rect(screen, BLACK, (276, 316, 50, 6))
def A3LL():
    pygame.draw.rect(screen, BLACK, (276, 344, 50, 6))
def F3LL():
    pygame.draw.rect(screen, BLACK, (276, 372, 50, 6))

#Game Loop
while notesPassed <= numberOfNotes:
    for event in pygame.event.get():
        print("Notes passed: " + str(notesPassed))
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == TIMER_EVENT:
            currentNoteIndex = random.randint(noteStart,noteEnd)#random.randint(0, len(TrebleNotes)-1)
            selection.append(TrebleNotes[currentNoteIndex])

            notesPassed+=1
            screen.fill(WHITE)
            screen.blit(backgroundIMG, (0, 140))

            if (currentNoteIndex == 0): # A6
                screen.blit(noteIMGF, (240, 35))  
                A5LL()
                C6LL()
                E6LL()
                G6LL()
            elif (currentNoteIndex == 1): #G6
                screen.blit(noteIMGF, (240, 49))
                A5LL()
                C6LL()
                E6LL()
                G6LL()
            elif (currentNoteIndex == 2): #F6
                screen.blit(noteIMGF, (240, 63))
                A5LL()
                C6LL()
                E6LL()
            elif (currentNoteIndex == 3): #E6
                screen.blit(noteIMGF, (240, 77))
                A5LL()
                C6LL()
                E6LL()
            elif (currentNoteIndex == 4): #D6
                screen.blit(noteIMGF, (240, 91))
                A5LL()
                C6LL()
            elif (currentNoteIndex == 5): #C6
                screen.blit(noteIMGF, (240, 105))
                A5LL()
                C6LL()
            elif (currentNoteIndex == 6): #B5
                screen.blit(noteIMGF, (240, 119))
                A5LL()
            elif (currentNoteIndex == 7): #A5
                screen.blit(noteIMGF, (240, 133))
                A5LL()
            elif (currentNoteIndex == 8): #G5
                screen.blit(noteIMGF, (240, 147))
            elif (currentNoteIndex == 9): #F5
                screen.blit(noteIMGF, (240, 161))
            elif (currentNoteIndex == 10): #E5
                screen.blit(noteIMGF, (240, 175))
            elif (currentNoteIndex == 11): #D5
                screen.blit(noteIMGF, (240, 189))
            elif (currentNoteIndex == 12): #C5
                screen.blit(noteIMGF, (240, 203))
            elif (currentNoteIndex == 13): #B4
                screen.blit(noteIMG, (250, 134))
            elif (currentNoteIndex == 14): #A4
                screen.blit(noteIMG, (250, 148))
            elif (currentNoteIndex == 15): #G4
                screen.blit(noteIMG, (250, 162))
            elif (currentNoteIndex == 16): #F4
                screen.blit(noteIMG, (250, 176))
            elif (currentNoteIndex == 17): #E4
                screen.blit(noteIMG, (250, 190))
            elif (currentNoteIndex == 18): #D4
                screen.blit(noteIMG, (250, 204))
            elif (currentNoteIndex == 19): #C4
                screen.blit(noteIMG, (250, 218))
                C4LL()
            elif (currentNoteIndex == 20): #B3
                screen.blit(noteIMG, (250, 232))
                C4LL()
            elif (currentNoteIndex == 21): #A3
                screen.blit(noteIMG, (250, 246))
                C4LL()
                A3LL()
            elif (currentNoteIndex == 22): #G3
                screen.blit(noteIMG, (250, 260))
                C4LL()
                A3LL()
            elif (currentNoteIndex == 23): #F3
                screen.blit(noteIMG, (250, 274))
                C4LL()
                A3LL()
                F3LL()
            elif (currentNoteIndex == 24): #E3
                screen.blit(noteIMG, (250, 288))
                C4LL()
                A3LL()
                F3LL()
            else:
                print(currentNoteIndex)            
            
    # Check for key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(30)

# Puts answers to screen
screen.fill(WHITE)
for i in range(0, len(selection)-1):
        noteTXT = font.render(selection[i], True, BLACK)
        screen.blit(noteTXT, (noteX, noteY))
        noteX += fontSize * 2
        if ((i+1)%8 == 0):
            noteY += fontSize
            noteX = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # Check for key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        exit()

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(30)

# Quit Pygame
pygame.quit()
