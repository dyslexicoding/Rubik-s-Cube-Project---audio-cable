import detect_color
import numpy as np
import cv2
def run(img):
    cropimage = cv2.resize(img, (300, 300))
    faceletarray, cXarray, cYarray = detect_color.run(cropimage)
    xarray = []
    yarray = []
    orderedCx = np.sort(cXarray)
    orderedCy = np.sort(cYarray)
    print(orderedCx)
    lengthcX = len(orderedCx)
    lengthcY = len(orderedCy)
    i = 0
    for p in range(lengthcX):
        print(orderedCx[p])
        if (p == 0):
            xarray.append(orderedCx[p])
            i = i+1
        else:
            if (orderedCx[p] > (xarray[i-1] + 4*(faceletarray[1][3]/3))):
                xarray.append(xarray[i-1]+faceletarray[1][3])
                i = i+1
            if (orderedCx[p] > xarray[i-1] + 3*(faceletarray[1][3])/2):
                xarray.append(orderedCx[p])
                i = i+1


    i = 0
    for p in range(lengthcY):
        if (p == 0):
            yarray.append(orderedCy[p])
            i = i +1
        elif (orderedCy[p] > yarray[i - 1] + (faceletarray[1][4] / 2)):
            yarray.append(orderedCy[p])
            i = i+ 1

    print("xarray")
    print(xarray)
    print("yarray")
    print(yarray)
    pixelxarray = (xarray[0], xarray[1], xarray[2], xarray[0], xarray[1], xarray[2], xarray[0], xarray[1], xarray[2],xarray[3], xarray[4], xarray[5] ,xarray[3], xarray[4], xarray[5] ,xarray[3], xarray[4], xarray[5])
    pixelyarray = (yarray[0], yarray[0], yarray[0], yarray[1], yarray[1],yarray[1],yarray[2],yarray[2],yarray[2],yarray[0],yarray[0],yarray[0],yarray[1],yarray[1],yarray[1],yarray[2],yarray[2],yarray[2])

    return(cropimage, pixelxarray, pixelyarray)

path = r'C:\Users\polog\OneDrive\Documents\gorup project report\test\aditonal\1.jpg'
img = cv2.imread(path)
run(img)
array = [65, 91, 125, 168, 203, 235]
print(array)