
def run(mode, array):
    movearray = []
    solvearray = []
    finalsolve = []
    if (mode == 1):
        f=open("mix.txt", "r")
        if f.mode == 'r':
            face = 0
            rotations = 1
            solverotations = 1
            mixstring =f.read()
            length = len(mixstring)
            for x in range(length):
                print(mixstring[x])
                if (mixstring[x] == '2'):
                    rotations = 2
                elif (mixstring[x] == "'"):
                    rotations = -1
                    solverotations = 3
                else:
                    face = mixstring[x]
                    move = (face, rotations, 0)
                    solve = (face + str(solverotations) + ' ')
                    movearray.append(move)
                    solvearray.append(solve)
                    rotations = 1

        solvearray.append('      ')
        finalsolve = "".join(solvearray)
    elif (mode == 2):
        f = open("123.txt", "r")
        if f.mode == 'r':
            cubestring = f.read()
            face = 0
            rotations = 1
            length = int((len(array)-6)/3)
            for x in range(length):
                j = x*3
                face = array[j]
                if (array[j+1] == '1'):
                    rotations = 1
                elif (array[j+1] == '2'):
                    rotations = 2
                else:
                    rotations = -1

                move = (face, rotations, 0)
                movearray.append(move)




    return movearray, finalsolve


f=open("123.txt", "r")
if f.mode == 'r':
    cubestring =f.read()

movearray, finalsolve = run(2, cubestring)