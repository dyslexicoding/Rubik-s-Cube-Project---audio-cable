import guiconverter as gui
import asd as asd
import cv2



def rungui():

    cubeletmap = gui.run()
    solvevid = asd.main(cubeletmap)
    print("hey")

rungui() #uncomment for testting




def coloursinimage(img):

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    masky = cv2.inRange(hsv, (15, 30, 20), (50, 255, 255))
    maskb = cv2.inRange(hsv, (100, 100, 20), (120, 255, 255))
    maskg = cv2.inRange(hsv, (50, 100, 20), (90, 255, 255))
    masko = cv2.inRange(hsv, (6, 20, 20), (30, 255, 255))
    maskr = cv2.inRange(hsv, (0, 0, 0), (30, 255, 255))
    maskw = cv2.inRange(hsv, (10, 0, 20), (255, 200, 255))
    maskarray = (masky, maskb, maskg, masko, maskr, maskw)
    return maskarray

path = r'C:\Users\polog\OneDrive\Documents\RubixMain\Rubix\Rubix\Photos\real\real1.jpg'
img = cv2.imread(path)
img = cv2.resize(img, (300, 300))