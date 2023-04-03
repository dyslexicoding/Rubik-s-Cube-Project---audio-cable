

def organise(cubestring):

    newcubestring = [0] * 54

    anticlock = [15, 12, 9, 16, 13, 10, 17, 14, 11]
    reverse = [8, 7, 6, 5, 4, 3, 2, 1, 0]

    for x in range(54):
        if (x<9):
            newcubestring[x] = cubestring[x]
        elif(x<18):
            newx = anticlock[x-9]
            newcubestring[x] = cubestring[newx]
        elif(x<27):
            newx = anticlock[x-18] + 9
            newcubestring[x] = cubestring[newx]
        elif (x < 36):
            newx = anticlock[x - 27] + 18
            newcubestring[x] = cubestring[newx]
        elif (x<45):
            newx = reverse[x-36] + 36
            newcubestring[x] = cubestring[newx]
        elif (x < 54):
            newx = reverse[x - 45] + 45
            newcubestring[x] = cubestring[newx]

    return (newcubestring)
