import cv2
def coloursinimage(img, colourchange):

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    masky = cv2.inRange(hsv, (15, 30, 20), (50, 255, 255))
    maskb = cv2.inRange(hsv, (100, 100, 20), (120, 255, 255))
    maskg = cv2.inRange(hsv, (50, 100, 20), (90, 255, 255))
    masko = cv2.inRange(hsv, (0, 200, 200), (2, 255, 255))
    maskr = cv2.inRange(hsv, (0, 50, 0), (200, 255, 255))
    maskw = cv2.inRange(hsv, (10, 0, 20), (255, 200, 255))
    maskarray = (masky, masko, maskr, maskb, maskg, maskw)

    return maskarray



def run():
    import OrganiseCube as org
    import CropImage as crop





    img = 0
    cubemultiply = 0
    colorarray = [0] * 54
    realcolor = [0] * 54
    searcharray = [0, 0, 5, 0, 0, -5, -5, 0, 0, 5, 5, 5, 5, -5, -5, -5, -5, 5]



    for k in range (3):




        print ("new image")

        if (k == 0):
            path = r'C:\Users\polog\OneDrive\Documents\RubixMain\Rubix\Rubix\Photos\real\real1.jpg'
            img = cv2.imread(path)
            (img, pixelxarray, pixelyarray) = crop.crop(img)
            cv2.imshow('img1', img)
            print ("pixelxarray")
            print(pixelxarray)
            print("pixelyarray")
            print(pixelyarray)
            cv2.imwrite(r'C:\Users\Caleb Fellows\Documents\Rubix\Rubix\Rubix\Photos\real\result.jpg', img)
        elif (k == 1):
            path = r'C:\Users\polog\OneDrive\Documents\RubixMain\Rubix\Rubix\Photos\real\real2.jpg'
            img = cv2.imread(path)
            (img, pixelxarray, pixelyarray) = crop.crop(img)
            cv2.imshow('img2', img)
            print("pixelxarray")
            print(pixelxarray)
            print("pixelyarray")
            print(pixelyarray)
            cv2.imwrite(r'C:\Users\Caleb Fellows\Documents\Rubix\Rubix\Rubix\Photos\real\result.jpg', img)

            cubemultiply = 1
        elif (k == 2):
            path = r'C:\Users\polog\OneDrive\Documents\RubixMain\Rubix\Rubix\Photos\real\real3.jpg'
            img = cv2.imread(path)
            (img, pixelxarray, pixelyarray) = crop.crop(img)
            cv2.imshow('img3', img)
            print("pixelxarray")
            print(pixelxarray)
            print("pixelyarray")
            print(pixelyarray)
            cv2.imwrite(r'C:\Users\Caleb Fellows\Documents\Rubix\Rubix\Rubix\Photos\real\result.jpg', img)
            cubemultiply = 2

        colourchange = (0,0,0,0,0,0)
        maskarray = coloursinimage(img, colourchange)
        cv2.waitKey(0)
        height = img.shape[1]
        width = img.shape[0]




        for  i in range(0, 18):

            search = 0
            searchmultiply = 1
            while (colorarray[i+18*cubemultiply] == 0):
                searchnumberx = (searchmultiply * searcharray[search])
                searchnumbery = (searchmultiply * searcharray[search+1])
                x = (pixelxarray[i] + searchnumberx)
                y = (pixelyarray[i] + searchnumbery)


                if ((search == 16)):
                    search = 0
                    searchmultiply = searchmultiply + 1

                if ((search == 2 and searchmultiply == 1)):
                    print("error")
                    print("x")
                    print(x - 5)
                    print("y")
                    print(y)

                search = search + 2


                if ((y < width) and (y> 0) and (x < height) and (x> 0)):

                    if ((maskarray[0])[y, x] == 255):
                        colorarray[i+18*cubemultiply] = "U"
                    elif ((maskarray[1])[y, x] == 255):
                        colorarray[i + 18 * cubemultiply] = "B"
                    elif ((maskarray[2])[y, x] == 255):
                        colorarray[i+18*cubemultiply] = "F"
                    elif ((maskarray[3])[y, x] == 255):
                        colorarray[i+18*cubemultiply] = "L"
                    elif ((maskarray[4])[y, x] == 255):
                        colorarray[i+18*cubemultiply] = "R"
                    elif ((maskarray[5])[y, x] == 255):
                        colorarray[i+18*cubemultiply] = "D"







    print(colorarray)
    print("1")

    f = open("originalcubestring.txt", "w+")
    for x in range(0, len(colorarray), 1):
        f.write(colorarray[x])
    f.close()

    colorarray = org.organise(colorarray)
    f= open("cubestring.txt","w+")
    for x in range(0, len(colorarray),1):
          f.write(colorarray[x])
    f.close()



run()
