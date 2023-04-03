import numpy as np
import pygame
import cv2
import CropImage as crop
import pygame.locals
import time
import destrou as dest
def run():
    returnarray = np.zeros((3, 2))
    returnarray[0][1] = 400
    returnarray[1][1] = 800
    returnarray[2][1] = 1200
                    # Capture frame-by-frame
    cap = cv2.VideoCapture(0)
    cap1 = cv2.VideoCapture(1)
    cap2 = cv2.VideoCapture(2)

    ret, frame = cap.read()
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()
    camera1 = (ret, frame)
    camera2 = (ret1, frame1)
    camera3 = (ret2, frame2)
    cameraarray = (camera1, camera2, camera3)
    for p in range(3):
        if (cameraarray[p][0] == False):
            returnarray[p][0] = False
        else:
            returnarray[p][0] = True
            frame = cameraarray[p][1]

            #(frame, x, y) = crop.crop(frame)
            frame = cv2.resize(frame, (300, 300))
            # Our operations on the frame come here
            cv2.imwrite((r'C:\Users\polog\OneDrive\Documents\RubixMain\Rubix\Rubix\Photos\real\camtest%d.jpg' % p),
                        frame);


                # Display the resulting frame




        # When everything done, release the capture
    cv2.destroyAllWindows()
    return (returnarray)

run()
