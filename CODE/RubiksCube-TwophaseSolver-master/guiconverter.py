import numpy as np

def run():
    f = open("originalcubestring.txt", "r")
    if f.mode == 'r':
        cubestring = f.read()
    print("2D array")
    print(cubestring)
    cubeletmap = np.zeros((27, 6))
    temp = np.zeros((27, 6))

    checkarray = ((24, 42, 80, 80,  80, 6), (80, 43, 80, 80, 80, 3), (80, 44, 51, 80, 80, 0), (25, 39, 80, 80, 80, 80), (80, 40, 80, 80, 80, 80), (80, 41,48, 80, 80, 80), (26,36, 80, 80, 33, 80), (80, 37, 80, 80, 34, 80), (80,38, 45, 80, 35, 80),
                  (21, 80, 80, 80, 80, 7), (80, 80, 80, 80, 80, 4), (80, 80, 52, 80, 80, 1), (22, 80, 80, 80, 80, 80), (80, 80, 80, 80, 80, 80), (80, 80, 49, 80, 80, 80),(23, 80, 80, 80, 30, 80), (80, 80, 80, 80, 31, 80), (80, 80, 46, 80, 32, 80),
                  (18, 80, 80, 15,80, 8), (80, 80, 80, 12, 80, 5), (80, 80, 53, 9, 80, 2), (19, 80, 80, 16, 80, 80), (80, 80, 80, 13, 80, 80), (80, 80, 50, 10, 80, 80), (20, 80, 80, 17, 27, 80), (80, 80, 80, 14, 28, 80), (80, 80, 47, 11, 29, 80))



    for x in range(27):
        for y in range(6):
            cubeletmap[x][y] = 6

    for x in range(27):
        for y in range(6):
            position =int(checkarray[x][y])

            if (checkarray[x][y] != 80):
                color, oppcolor = colourcheck(cubestring[position])

                cubeletmap[x][y] = color
                #if (y == 0):
                #    cubeletmap[x][2] = oppcolor
                #if (y == 1):
                #    cubeletmap[x][3] = oppcolor
                #if (y == 2):
                #    cubeletmap[x][0] = oppcolor
                #if (y == 3):
                #    cubeletmap[x][1] = oppcolor
                #if (y == 4):
                #    cubeletmap[x][5] = oppcolor
                #if (y == 5):
                #    cubeletmap[x][4] = oppcolor
    print("3D array")
    print(cubeletmap)



    return(cubeletmap)


def colourcheck(Position):
    if (Position == "L"):
        colour = 1
        colourreverse = 3
    elif (Position == "F"):
        colour = 0
        colourreverse = 2
    elif (Position == "R"):
        colour = 3
        colourreverse = 1
    elif (Position == "U"):
        colour = 5
        colourreverse = 4
    elif (Position == "D"):
        colour = 4
        colourreverse = 5
    else:
        colour = 2
        colourreverse = 0




    return(colour, colourreverse)

