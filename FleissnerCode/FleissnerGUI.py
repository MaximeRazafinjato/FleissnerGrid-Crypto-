# -------------------------------------------------------------------
# ------------------------------IMPORTS------------------------------
# -------------------------------------------------------------------
import pygame, sys
from pygame.locals import *
from algorithmsFleissner import *
pygame.init()
# -------------------------------------------------------------------
# ------------------------------COLORS-------------------------------
# -------------------------------------------------------------------

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (150, 150, 150)
RED = (150, 0, 0)
BRIGHT_RED = (255, 0, 0)
GREEN = (0, 150, 0)
BRIGHT_GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
ORANGE = (255, 106, 0)
PURPLE = (157, 0, 255)


widthCell = 80
lengthCell = 80
startPosX = 5
startPosY = 5
displayWidth = 800
displayHeight = 600

mySurface = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("Fleissner grid")
clock = pygame.time.Clock()

# -------------------------------------------------------------------
# -----------------------------FUNCTIONS-----------------------------
# -------------------------------------------------------------------


def click(mouseX, mouseY, x, y, width, height):
    if mouseX > x and mouseX < x + width and mouseY > y and mouseY < y + height:
        return True
    else:
        return False


def inputGrid(mySurface, grid, n):

    global startPosX
    global startPosY
    i = 0
    j = 0

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                mouseX = event.pos[0]
                mouseY = event.pos[1]

                # ------------ Selecting Cell ----------------
                startY = startPosY
                for x in range(n):
                    startX = startPosX
                    r = x
                    for y in range(n):
                        c = y
                        if startX + widthCell > mouseX > startX and startY + lengthCell > mouseY > startY:
                            i = r
                            j = c
                            break
                        startX += widthCell
                    startY += lengthCell
                position = (i, j)
                print(position)

                # --------- updating board -------------

                if possible(grid, n, i, j) == 1:
                    put(grid, n, i, j)
                    saveGrid(grid, n, 'key')


            mySurface.fill(BLACK)
            drawGrid(mySurface, n)
            drawCell(mySurface, grid, n)

            if 0 not in grid:
                continue

        pygame.display.update()


def drawCell(mySurface, grid, n):

    for r in range(n):
        for c in range(n):
            x = r+1
            y = c+1
            color_selected = WHITE
            color_rotated = GREY
            if grid[r][c] == 1:
                pygame.draw.rect(mySurface, color_selected, ((startPosX + (widthCell*(y-1))+5.7),
                                                (startPosY + (lengthCell*(x-1))+5.7), widthCell-10, lengthCell-10), 0)
            if grid[r][c] == 2:
                pygame.draw.rect(mySurface, color_rotated, ((startPosX + (widthCell*(y-1))+5.7),
                                                (startPosY + (lengthCell*(x-1))+5.7), widthCell-10, lengthCell-10), 0)


def drawGrid(mySurface, n):

    posX = startPosX
    posY = startPosY
    for x in range(n):
        for y in range(n):
            pygame.draw.polygon(mySurface, RED, (
                (posX, posY), (posX, posY + lengthCell), (posX + widthCell, posY + lengthCell),
                (posX + widthCell, posY)),
                                5)
            posX += widthCell
        posX = startPosX
        posY += lengthCell

# -------------------------------------------------------------------
# --------------------------Main function----------------------------
# -------------------------------------------------------------------


def FleissnerGrid(n):
    global displayWidth
    global displayHeight

    grid = randomGrid(n)
    mySurface = pygame.display.set_mode(((widthCell*n)+(2*startPosX), (lengthCell*n)+(2*startPosY)))
    inputGrid(mySurface, grid, n)
    pygame.display.update()

    return grid


FleissnerGrid(6)





#for r in range(n):
#        for c in range(n):
#            x, y = 0, 0

#            if player1 == True:
#                if grid[x][y] == 'O':

#                    # Check la case au-dessus
#                    if grid[x - 1][y] == ' ':
#                        grid[x - 1][y] == '.'
#                    else:
#                        continue

#                    # Check la case au-dessous
#                    if grid[x + 1][y] == ' ':
#                        grid[x + 1][y] == '.'
#                    else:
#                        continue

#                    # Check la case à gauche
#                    if grid[x][y - 1] == ' ':
#                        grid[x][y - 1] == '.'
#                    else:
#                        continue

#                    # Check la case à droite
#                    if grid[x][y + 1] == ' ':
#                        grid[x][y + 1] == '.'
#                    else:
#                        continue

#            if player2 == True:
#                if grid[x][y] == 'O':

#                    # Check la case au-dessus
#                    if grid[x - 1][y] == ' ':
#                        grid[x - 1][y] == '.'
#                    else:
#                        continue

#                    # Check la case au-dessous
#                    if grid[x + 1][y] == ' ':
#                        grid[x + 1][y] == '.'
#                    else:
#                        continue

#                    # Check la case à gauche
#                    if grid[x][y - 1] == ' ':
#                        grid[x][y - 1] == '.'
#                    else:
#                        continue

#                    # Check la case à droite
#                    if grid[x][y + 1] == ' ':
#                        grid[x][y + 1] == '.'
#                    else:
#                        continue
