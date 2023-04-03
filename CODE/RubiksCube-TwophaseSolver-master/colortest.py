import cv2


pixelxarray = [70,100, 125, 65, 95, 135, 67, 92, 130, 170, 205, 234, 170, 206, 236, 170, 205, 234]
pixelyarray = [86, 80,74, 150, 148, 150, 213, 218, 228, 75, 80, 87, 153, 150, 153, 230, 223, 217]


img = 0
cubemultiply = 0
colorarray = [0] * 54
searcharray = [0, 0, 5, 0, 0, -5, -5, 0, 0, 5, 5, 5, 5, -5, -5, -5, -5, 5]



for k in range (3):
    search = 0
    searchmultiply = 1
    print ("new image")
    search = 0

    if (k== 0):
        path = r'C:\Users\polog\OneDrive\Documents\gorup project report\Final Test\moves\camtest1.png'
        img = cv2.imread(path)
        img = cv2.resize(img, (300, 300))
        cv2.imwrite(r"C:\Users\Caleb Fellows\Documents\Rubix\Photos\y.jpg", img);
        cv2.imshow('img1', img)
    elif (k== 1):
        path = r'C:\Users\Caleb Fellows\Documents\Rubix\Photos\real2.jpg'
        img = cv2.imread(path)
        img = cv2.resize(img, (300, 300))
        cv2.imshow('img2', img)

        cubemultiply = 1
    elif (k == 2):
        path = r'C:\Users\Caleb Fellows\Documents\Rubix\Photos\real3.jpg'
        img = cv2.imread(path)
        img = cv2.resize(img, (300, 300))
        cv2.imshow('img3', img)
        cubemultiply = 2


    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    thresh = cv2.inRange(hsv, (0, 0, 100), (255, 255, 255))

    cv2.imshow("Thresh", thresh)
    masky = cv2.inRange(hsv, (15, 30, 20), (50, 255, 255))
    maskb = cv2.inRange(hsv, (100, 100, 20), (120, 255, 255))
    maskg = cv2.inRange(hsv, (50, 100, 20), (90, 255, 255))
    masko = cv2.inRange(hsv, (0, 200, 200), (2, 255, 255))
    maskr = cv2.inRange(hsv, (0, 50, 0), (200, 255, 255))
    maskw = cv2.inRange(hsv, (10, 0, 20), (255, 200, 255))

    #masky = cv2.inRange(hsv, (15, 30, 20), (50, 255, 255))
    cv2.imshow("yellow", masky);


    #maskr = cv2.inRange(hsv, (50, 50, 20), (210, 255, 255))
    cv2.imshow("red", maskr);

    lower = (255, 55, 0)  # lower bound for each channel
    upper = (255, 255, 10)  # upper bound for each channel

    # create the mask and use it to change the colors
    #mask = cv2.inRange(img, lower, upper)

    # display it
    #cv2.imshow("frame", mask)
    cv2.waitKey(1)


    #maskb = cv2.inRange(hsv, (100, 100, 20), (120, 255, 255))
    cv2.imshow("blue", maskb);
    #maskg = cv2.inRange(hsv, (50, 100, 20), (90, 255, 255))
    cv2.imshow("green", maskg);
    #masko = cv2.inRange(hsv, (3, 100, 20), (15, 255, 255))
    cv2.imshow("orange", masko);
    #maskw = cv2.inRange(hsv, (10, 0, 20), (255, 200, 255))
    cv2.imshow("white", maskw);
    #maskbl = cv2.inRange(hsv, (0, 0, 140), (255, 255, 255))
    #cv2.imshow("black", maskbl);

    cv2.waitKey();
    cv2.destroyAllWindows()

    [61, 90, 124, 61, 90, 124, 61, 90, 124, 163, 191, 215, 163, 191, 215, 163, 191, 215]
    [142, 142, 142, 181, 181, 181, 219, 219, 219, 142, 142, 142, 181, 181, 181, 219, 219, 219]