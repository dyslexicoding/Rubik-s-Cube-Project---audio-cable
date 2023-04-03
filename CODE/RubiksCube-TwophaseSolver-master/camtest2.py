import cv2

def run():
    cap = cv2.VideoCapture(0)

    ret, frame = cap.read()


    # frame = cv2.resize(frame, (300, 300))

    # Our operations on the frame come here

    # Display the resulting frame
    cv2.imwrite((r'C:\Users\polog\OneDrive\Documents\RubixMain\Rubix\Rubix\Photos\real\camtest%s.jpg' % 2), frame);

run()