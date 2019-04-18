import random
import copy

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
           "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
clock = True


# sandorf = [[0, 1, 0, 1, 0, 1], [0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0],
# [0, 1, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1], [0, 0, 0, 1, 0, 0]]

# -------------------------------------------------------------------
# ----------------------------Functions------------------------------
# -------------------------------------------------------------------


# remove punctuation marks and spaces
def clear(word):
    word = word.replace(' ', '')
    word = word.replace('.', '')
    word = word.replace(',', '')
    word = word.replace('?', '')
    word = word.replace('!', '')
    word = word.replace(':', '')
    word = word.replace(';', '')
    word = word.replace('-', '')
    word = word.replace('"', '')
    word = word.replace('á', 'a')
    word = word.replace('à', 'a')
    word = word.replace('â', 'a')
    word = word.replace('é', 'e')
    word = word.replace('è', 'e')
    word = word.replace('ê', 'e')
    word = word.replace("'", '')
    word = word.lower()

    return word


# where text is a string and will return it after removing spaces, punctuations marks, etc
def convertLetters(text):
    text = clear(text)
    return text


# returns string of concatenated text, if it's too short, will choose random letters to fill up the number of squares
def completion(text, n):
    if len(text) < ((n * n)/4)*4:
        while len(text) < ((n * n)/4)*4:
            text = text + letters[random.randint(-1, 25)]
    return text


# saves in the file named file the content of the grid
def saveGrid(grid, n, file):

    grid = str(grid)
    file = str(file)
    f = open(file + '.txt', 'w')
    f.write(grid)
    f.close()


# returns corresponding data contained in the file named "file"
def loadGrid(file):
    arr = []
    inp = open(file + ".txt", "r")
    # read line into array
    for line in inp.readlines():
        # add a new sublist
        arr.append([])
        # loop over the elemets, split by whitespace
        for i in line.split():
            # convert to integer and append to the last
            # element of the list
            arr[-1].append(int(i))
    return arr

# check if the grid is a Fleissner grid
def correct(grid, n):

    for x in range(n):
        for y in range(n):
            if (grid[x][y] and rotation(grid, n, clock)[x][y] == 1
                    or grid[x][y] and rotation(rotation(grid, n, clock), clock, n)[x][y] == 1
                    or grid[x][y] and rotation(rotation(rotation(grid, n, clock), clock, n), clock, n) == 1):
                print('The Grid is not a Fleissner one !!!')
                return False
    return True


def count(grid, n):
    nbsquare = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                nbsquare += 1

# Create a grid
def randomGrid(n):
    grid = []
    for x in range(n):
        grid += [[0] * n]
    return grid


# Function used in GUI to enable a click on a square or not
def possible(grid, n, i, j):
    # if n % 2 == 1:
    #     print((n-1)/2)
    #     if grid[int((n-1)/2)][int((n-1)/2)]:
    #         return False
    if grid[i][j] == 1:
        return False
    elif grid[i][j] == 2:
        return False
    else:
        return True


# function used in GUI to select a square
def put(grid, n, i, j):
    # Cannot select the middle square if n is odd
    if n % 2 == 1:
        print((n - 1) / 2)
        grid[int((n - 1) / 2)][int((n - 1) / 2)] = 2
    grid[i][j] += 1
    rotation(grid, n, clock)
    grid[i][j] += 2
    rotation(grid, n, clock)
    grid[i][j] += 2
    rotation(grid, n, clock)
    grid[i][j] += 2
    rotation(grid, n, clock)


# Rotates the grid 90° clockwise
def rotation(grid, n, clock):
    for row in range(len(grid)):
        for columns in range(row, len(grid)):
            x = grid[row][columns]
            y = grid[columns][row]
            grid[row][columns] = y
            grid[columns][row] = x

    for index, row in enumerate(grid):
        grid[index] = list(reversed(row))
    return grid


# returns a square of the same size as the grid which contains encrypted text by the grid
def cipher(grid, n, text, clock):
    square = copy.deepcopy(grid)
    x = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                square[i][j] = text[x]
                x = x + 1
    # print(square)

    rotation(grid, n, clock)
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                square[i][j] = text[x]
                x = x + 1
    # print(square)

    rotation(grid, n, clock)
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                square[i][j] = text[x]
                x = x + 1
    # print(square)

    rotation(grid, n, clock)
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                square[i][j] = text[x]
                x = x + 1
    # print(square)
    return square


# From the square, print the text ciphered
def squareToText(square, n):
    text = ""
    for i in square:
        for j in i:
            text += str(j)
    return text


# Use the some of precedent functions to cipher the text
def cipherFleissner (grid, n, text, clock):
    text = convertLetters(text)
    text = completion(text, n)
    if correct(grid, n) == 1:
        square = cipher(grid, n, text, clock)
        text = squareToText(square, n)
    return text


# Prints the text ciphered in square
def textToSquare(text, n):
    square = []
    y = 0
    for x in range(n):
        square += [[] * n]
    for i in range(n):
        for j in range(n):
            square[i] = square[i] + list(text[y])
            y += 1
    return square


def decipher(grid, n, square, clock):
    textDeciphered = ''

    # rotation to put the grid in the right direction
    rotation(grid, n, clock)
    rotation(grid, n, clock)
    rotation(grid, n, clock)

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                textDeciphered += square[i][j]

    rotation(grid, n, clock)
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                textDeciphered += square[i][j]

    rotation(grid, n, clock)
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                textDeciphered += square[i][j]

    rotation(grid, n, clock)
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                textDeciphered += square[i][j]
    return textDeciphered


# Use the some of the precedent functions to decipher the text
def decipherFleissner(grid, n ,text, clock):
    if correct(grid, n) == 1:
        grid = rotation(grid, n, clock)
        square = textToSquare(text, n)
        text = decipher(grid, n, square, clock)
    return text


# TEST #
key = [[2, 1, 2, 2, 2, 2], [2, 2, 2, 2, 1, 2], [2, 2, 1, 2, 2, 2], [1, 2, 2, 2, 1, 2], [2, 2, 2, 1, 2, 1], [2, 2, 1, 2, 2, 1]] # This should be read from the created key.txt
n = len(key)
for i in range(n):
    for j in range(n):
        if key[i][j] == 2:
            key[i][j] = 0
print(key)
c = cipherFleissner(key, n, "Your mouth don't move but I can hear you speak", clock)
print(c)
d = decipherFleissner(key, n, c, clock)
print(d)

# The main problem is when I try to import the key from the text file.
# The input I get is not an array but series of character so when I try to take the length of it,
# Instead of getting something like 6 I have 80 which is, as I said the number of character including brackets and comas

# The following part is what I used to do if the import part was correct
# Transform all 2s used for the GUI in 0s for the grid for the next part of the program
# for i in range(n):
#     for j in range(n):
#         if grid[i][j] == 2:
#             grid[i][j] = 0




