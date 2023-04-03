import pygame as pg
import rungui
import camtest
import cv2
import example

def main():
    pg.init()
    screen = pg.display.set_mode((1920, 1080), pg.FULLSCREEN)
    font1 = pg.font.Font(None, 64)

    clock = pg.time.Clock()
    transparent = pg.Color('black')
    textcolour = pg.Color('white')
    font = pg.font.Font('freesansbold.ttf', 18)
    color_inactive = pg.Color('lightskyblue3')
    color_active = pg.Color('dodgerblue2')
    input_box1 = pg.Rect(390, 185, 320, 240)
    input_box2 = pg.Rect(790, 185, 320, 240)
    input_box3 = pg.Rect(1190, 185, 320, 240)
    solveRect = pg.Rect(878, 700, 144, 45)
    active1 = False
    active2 = False
    active3 = False
    activesolve = False
    activecolourY = False
    activecolourO = False
    activecolourR = False
    activecolourB = False
    activecolourG = False
    activecolourW = False
    activecolourarray = [[pg.K_y,activecolourY],[pg.K_o, activecolourO],[pg.K_r, activecolourR], [pg.K_b, activecolourB], [pg.K_g, activecolourG], [pg.K_w, activecolourW]]
    colourchange = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    inputbox1 = [input_box1, active1, color_inactive]
    inputbox2 = [input_box2, active2, color_inactive]
    inputbox3 = [input_box3, active3, color_inactive]
    solvebox = [solveRect, activesolve, 0]
    inputboxarray = [inputbox1, inputbox2, inputbox3, solvebox]
    colourarray = ((390, 415), (790, 415), (1190, 415), (390, 635), (790, 635), (1190, 635))
    textarray = ('Yellow', 'Orange', 'Red', 'Blue', 'Green', 'White')
    red = pg.Color('red')
    green = pg.Color('green')
    color = color_inactive
    text = ''
    done = False
    shot = 0
    colour = 4
    rectcount = 0
    cap = cv2.VideoCapture(0)
    cap1 = cv2.VideoCapture(1)
    cap2 = cv2.VideoCapture(2)
    while not done:
        rectcount = 0
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                for rect in range(len(inputboxarray)):

                    if inputboxarray[rect][0].collidepoint(event.pos):
                        # Toggle the active variable.
                        inputboxarray[rect][1] = not inputboxarray[rect][1]

                    else:
                        inputboxarray[rect][1] = False
                    # Change the current color of the input box.
                    if (rect != 3):
                        if inputboxarray[rect][1]:
                            inputboxarray[rect][2] = color_active
                            colour = rect
                        else:
                            inputboxarray[rect][2] = color_inactive
                            rectcount = rectcount+1

            if color !=4:
                if event.type == pg.KEYDOWN:
                    print(activecolourarray)
                    for key in range(6):
                        if event.key == activecolourarray[key][0]:
                            activecolourarray[key][1] = not activecolourarray[key][1]
                        if event.key == pg.K_UP and activecolourarray[key][1] == True:
                            colourchange[key] = colourchange[key] + 1
                        elif event.key == pg.K_DOWN  and activecolourarray[key][1] == True:
                            colourchange[key] =  colourchange[key] -1
                        elif event.key == pg.K_LEFT and activecolourarray[key][1] == True:
                            colourchange[key+6] = colourchange[key+6] + 1
                        elif event.key == pg.K_RIGHT and activecolourarray[key][1] == True:
                            colourchange[key+6] = colourchange[key+6] - 1




        # Render the current text.
        # Resize the box if the text is too long.
        # Blit the text.
        # Blit the input_box rect.

        text1 = font1.render('SOLVE', True, textcolour)
        screen.blit(text1, solveRect)

        print(rectcount)
        if (rectcount == 3):
            colour = 4
            xx = int(colourarray[x][0])
            yy = int(colourarray[x][1])


            blackrect = pg.Rect(0, 0, 2000, 2000)
            pg.draw.rect(screen, transparent, blackrect)

        cameraarray, length = camtest.run(colour, cap, cap1, cap2, colourchange)
        for p in range(3):
            if(cameraarray[p][0] == True):
                camera = pg.image.load(r'C:\Users\polog\OneDrive\Documents\RubixMain\Rubix\Rubix\Photos\real\camtest%d.jpg' %p)
                screen.blit(camera, (cameraarray[p][1], 155))
            else:
                pass

        for x in range(6):
            if (colour != 4):
                camera = pg.image.load(r'C:\Users\polog\OneDrive\Documents\RubixMain\Rubix\Rubix\Photos\real\colour%d.jpg' % x)
                screen.blit(camera, (colourarray[x][0], colourarray[x][1]))
                if activecolourarray[x][1] == True:
                    textcolour = color_active
                else:
                    textcolour = color_inactive
                text = font.render(textarray[x], True, textcolour)
                textRect = text.get_rect()
                textRect.center = ((colourarray[x][0]+50), colourarray[x][1]+50)

                screen.blit(text, textRect)
            #elif(colour == 4):
            #    print("hye")
            #    xx = int (colourarray[x][0])
            #    yy = int (colourarray[x][1])
            #    blackrect = pg.Rect(0, 0, 2000, 2000)
            #    pg.draw.rect(screen, transparent, blackrect)
        #400-1800


        if (inputboxarray[3][1] == True):
            done == True
            pg.quit()
            example.run()

        for p in range(len(inputboxarray)):
            pg.draw.rect(screen, inputboxarray[p][2], inputboxarray[p][0], 2)



        pg.display.flip()
        clock.tick(30)


def animatecube(shot):
    if (shot == 0):
        rungui.rungui
    elif (shot > 130):
        shot = 1
    shot = shot + 1
    Img = pg.image.load(r'C:\Users\polog\OneDrive\Documents\RubixMain\Rubix\Rubix\Photos\real\shot%d.jpg' % shot)

    return (shot, Img)



#rungui.rungui()
main()