
import pyaudio
import numpy as np
import time
import pygame
def run(moves, x, animate):



    p = pyaudio.PyAudio()

    Up = ["U", 1500, pygame.K_2, pygame.K_F2]
    Right = ["R", 4500, pygame.K_4, pygame.K_F4]
    Forward = ["F", 8000, pygame.K_3, pygame.K_F3]
    Down = ["D", 12500, pygame.K_5, pygame.K_F5]
    Left = ["L", 15500, pygame.K_1, pygame.K_F1]
    Back = ["B", 18500, pygame.K_6, pygame.K_F6]
    movearray = [Up, Right, Forward, Down, Left, Back]

    volume = 0.5       # range [0.0, 1.0]
    fs = 44100         # sampling rate, Hz, must be integer
    if (animate == 1):
        duration = 0.001     # in seconds, may be float
    else:
        duration = 0.1

    volume = 0.5       # range [0.0, 1.0]
    fs = 44100         # sampling rate, Hz, must be integer
    duration = 0.1     # in seconds, may be float
    f = 440.0          # sine frequency, Hz, may be float

    invert = 0

    print(moves)
    print("lol")
    j = x*3
    print(moves[j + 1])
    if moves[j + 1] == "1":
        rotations = 1
        invert = 0
    elif moves[j + 1] == "2":
        rotations = 2
        invert = 0
    else:
        invert = 1
        rotations = 1


    for i in range(len(movearray)):
            if (moves[j] == movearray[i][0]):
                movement = movearray[i][2]
                f = movearray[i][1]
                if (invert == 1):
                    fr = 15000
                    movement = movearray[i][3]
                else:
                    fr = 0
                samplesL = (np.sin(2 * np.pi * np.arange(fs * duration) * f / fs)).astype(np.float32)
                samplesR = (np.sin(2 * np.pi * np.arange(fs * duration) * fr / fs)).astype(np.float32)
                print("hey")
                print(np.arange(fs*duration))
                stereo_signal = np.zeros([len(samplesL), 2])  # these two lines are new
                stereo_signal[:, 0] = samplesL[:]  # 1 for right speaker, 0 for  left
                stereo_signal[:, 1] = samplesR[:]

                for k in range(rotations):
                    print("w")
                    print(moves[j])
                    print(movearray[i][0])
                    stream = p.open(format=pyaudio.paFloat32,
                                        channels=2,
                                        rate=fs,
                                        output=True)

                    # play. May repeat with different volume values (if done interactively)
                    stream.write(volume * stereo_signal)



    return(movement, rotations)