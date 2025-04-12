#Crystal Long, Dario Gomez 4/12/2025 Assignmnet 6.2
"""Forest Fire Sim, modified by Sue Sampson, based on a program by Al Sweigart
A simulation of wildfires spreading in a forest. Press Ctrl-C to stop.
Inspired by Nicky Case's Emoji Sim http://ncase.me/simulating/model/
** use spaces, not indentation to modify **
Tags: short, bext, simulation"""

import random, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Set up the constants:
WIDTH = 79
HEIGHT = 22

TREE = 'A'
FIRE = '@'
EMPTY = ' '
LAKE = 's'

INITIAL_TREE_DENSITY = 0.20
GROW_CHANCE = 0.01
FIRE_CHANCE = 0.01
PAUSE_LENGTH = 0.5


def main():
    forest = createNewForest()
    bext.clear()

    while True:
        displayForest(forest)

        nextForest = {'width': forest['width'], 'height': forest['height']}

        for x in range(forest['width']):
            for y in range(forest['height']):

                if forest[(x, y)] == EMPTY and random.random() <= GROW_CHANCE:
                    nextForest[(x, y)] = TREE
                elif forest[(x, y)] == TREE and random.random() <= FIRE_CHANCE:
                    nextForest[(x, y)] = FIRE
                elif forest[(x, y)] == FIRE:
                    for ix in range(-1, 2):
                        for iy in range(-1, 2):
                            nx, ny = x + ix, y + iy
                            if forest.get((nx, ny)) == TREE:
                                nextForest[(nx, ny)] = FIRE
                    nextForest[(x, y)] = EMPTY
                else:
                    nextForest[(x, y)] = forest[(x, y)]

        forest = nextForest
        time.sleep(PAUSE_LENGTH)


def createNewForest():
    forest = {'width': WIDTH, 'height': HEIGHT}
    lakeCoords = set()

    # Define an irregular hardcoded lake pattern (s = water, space = not water)
    lakePattern = [
        "       sssss       ",
        "     sssssssss     ",
        "    sssssssssss    ",
        "    sssssssssss    ",
        "     sssssssss     ",
        "       sssss       ",
    ]

    lakeStartX = (WIDTH - len(lakePattern[0])) // 2
    lakeStartY = (HEIGHT - len(lakePattern)) // 2

    # Build lake coordinates from the pattern
    for dy, row in enumerate(lakePattern):
        for dx, char in enumerate(row):
            if char == 's':
                x = lakeStartX + dx
                y = lakeStartY + dy
                lakeCoords.add((x, y))

    # Populate the forest
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if (x, y) in lakeCoords:
                forest[(x, y)] = LAKE
            elif random.random() <= INITIAL_TREE_DENSITY:
                forest[(x, y)] = TREE
            else:
                forest[(x, y)] = EMPTY

    return forest



def displayForest(forest):
    bext.goto(0, 0)
    for y in range(forest['height']):
        for x in range(forest['width']):
            tile = forest[(x, y)]
            if tile == TREE:
                bext.fg('green')
                print(TREE, end='')
            elif tile == FIRE:
                bext.fg('red')
                print(FIRE, end='')
            elif tile == LAKE:
                bext.fg('blue')
                print(LAKE, end='')
            else:
                print(EMPTY, end='')
        print()
    bext.fg('reset')
    print('Grow chance: {}%  '.format(GROW_CHANCE * 100), end='')
    print('Lightning chance: {}%  '.format(FIRE_CHANCE * 100), end='')
    print('Press Ctrl-C to quit.')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
