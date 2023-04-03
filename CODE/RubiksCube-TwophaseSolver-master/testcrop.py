import cv2
img = 0
cropimg = 0
path = r'C:\Users\Caleb Fellows\Documents\Rubix\Photos\dark\3.jpg'
img = cv2.imread(path)
img = cv2.resize(img, (300, 300))

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
maskbl = cv2.inRange(hsv, (0, 0, 90), (255, 255, 255))
cv2.imshow("black", maskbl);
cv2.waitKey();cv2.destroyAllWindows()

height = img.shape[1]
width = img.shape[0]

possible = 0
toolarge = 0
squarecounter = 0
extentionx = 0
firstsquarex = [0, 0]
secondsquarex = [0, 0]
thirdsquarex = [0, 0]
fourthsquarex = [0, 0]
fifthsquarex = [0, 0]
sixthsquarex = [0, 0]
squarearrayx = [firstsquarex, secondsquarex, thirdsquarex, fourthsquarex, fifthsquarex, sixthsquarex]

while (squarearrayx[5][1] == 0):
    squarecounter = 0
    extentionx = extentionx - 5
    for i in range(width):


        j = int(height / 2) + extentionx
        print(j)

        p = maskbl[j, i]
        if (squarecounter == 6):
            break


        if p == 255:
            possible = possible + 1
            if (possible > 10):
                toolarge = toolarge + 1
        else:
            if (possible > 10 and toolarge < 30):
                squarearrayx[squarecounter][1] = i
                squarearrayx[squarecounter][0] = x
                squarecounter = squarecounter + 1


            possible = 0
            toolarge = 0

        if (possible == 1):
            x = i

print(squarearrayx)

possible = 0
toolarge = 0
squarecounter = 0
extensiony = 0
firstsquarey = [0, 0]
secondsquarey = [0, 0]
thirdsquarey = [0, 0]
squarearrayy = [firstsquarey, secondsquarey, thirdsquarey]

while (squarearrayy[2][1] == 0):
    squarecounter = 0
    extensiony = extensiony + 5
    for i in range(height):
        j = int((squarearrayx[3][0] + (squarearrayx[3][1] - squarearrayx[3][0]) / 2) + extensiony - 5)
        p = maskbl[i, j]
        if (squarecounter == 3):
            break

        if p == 255:
            possible = possible + 1
            if (possible >10):
                toolarge = toolarge + 1
        else:
            if (possible > 10 and toolarge < 55):
                squarearrayy[squarecounter][1] = i
                squarearrayy[squarecounter][0] = x
                squarecounter = squarecounter + 1
            possible = 0
            toolarge = 0

        if (possible == 1):
            x = i

cv2.imshow("black", maskbl);

crop_img = img[squarearrayy[0][0]:squarearrayy[2][1], squarearrayx[0][0]:squarearrayx[5][1]]
cv2.imshow("cropped", crop_img)
cv2.waitKey();
xpixelarray = [0] * 18
ypixelarray = [0] * 18
i = 0
for p in range(3):
    for o in range(3):
        xpixelarray[i] = int(squarearrayx[o][0] + ((squarearrayx[o][1] - squarearrayx[o][0]) / 2) - squarearrayx[0][0])
        i = i + 1

i = 0
for p in range(3):
    for o in range(3):
        xpixelarray[(i + 9)] = int(squarearrayx[o + 3][0] + ((squarearrayx[o + 3][1] - squarearrayx[o + 3][0]) / 2) - squarearrayx[0][0])
        i = i + 1


i = 0
for p in range(3):
    for o in range(3):
        ypixelarray[i] = int(squarearrayy[p][0] + ((squarearrayy[p][1] - squarearrayy[p][0]) / 2) - squarearrayy[0][0])
        i = i + 1

i = 0
for p in range(3):
    for o in range(3):
        ypixelarray[(i + 9)] = int(squarearrayy[p][0] + ((squarearrayy[p][1] - squarearrayy[p][0]) / 2) - squarearrayy[0][0])
        i = i + 1

print(xpixelarray)
print(ypixelarray)
cv2.imwrite(r'C:\Users\Caleb Fellows\Documents\Rubix\Photos\dark\dark1.jpg', crop_img)
cv2.destroyAllWindows()
