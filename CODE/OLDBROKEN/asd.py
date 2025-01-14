import pygame
import random
import audio
from pygame.locals import *
#import camtest2
import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    ( 1, -1, -1), ( 1,  1, -1), (-1,  1, -1), (-1, -1, -1),
    ( 1, -1,  1), ( 1,  1,  1), (-1, -1,  1), (-1,  1,  1)
)
edges = ((0,1),(0,3),(0,4),(2,1),(2,3),(2,7),(6,3),(6,4),(6,7),(5,1),(5,4),(5,7))
surfaces = ((0, 1, 2, 3), (3, 2, 7, 6), (6, 7, 5, 4), (4, 5, 1, 0), (1, 5, 7, 2), (4, 0, 3, 6))
#red,  blue, orange, green, white, yellow
colors = ((1, 0, 0), (0, 0, 1), (1, 0.5, 0), (0, 1, 0), (1, 1, 1), (1, 1, 0), (0,0,0))
bufarray = np.zeros((1000,80,80,3))

class Cube():
    def __init__(self, id, N, scale):
        self.N = N
        self.scale = scale
        self.init_i = [*id]
        self.current_i = [*id]
        self.rot = [[1 if i==j else 0 for i in range(3)] for j in range(3)]

    def isAffected(self, axis, slice, dir):
        return self.current_i[axis] == slice

    def update(self, axis, slice, dir):

        if not self.isAffected(axis, slice, dir):
            return

        i, j = (axis+1) % 3, (axis+2) % 3
        for k in range(3):
            self.rot[k][i], self.rot[k][j] = -self.rot[k][j]*dir, self.rot[k][i]*dir

        self.current_i[i], self.current_i[j] = (
            self.current_i[j] if dir < 0 else self.N - 1 - self.current_i[j],
            self.current_i[i] if dir > 0 else self.N - 1 - self.current_i[i] )

    def transformMat(self):
        scaleA = [[s*self.scale for s in a] for a in self.rot]
        scaleT = [(p-(self.N-1)/2)*2.1*self.scale for p in self.current_i]
        return [*scaleA[0], 0, *scaleA[1], 0, *scaleA[2], 0, *scaleT, 1]

    def draw(self, col, surf, vert, animate, angle, axis, slice, dir, k, cubeletmap):

        glPushMatrix()
        if animate and self.isAffected(axis, slice, dir):
            glRotatef( angle*dir, *[1 if i==axis else 0 for i in range(3)] )
        glMultMatrixf( self.transformMat() )



        glBegin(GL_QUADS)
        for i in range(6):
            constant = int (cubeletmap[k][i])

            glColor3fv(colors[constant])
            for j in surf[i]:
                glVertex3fv(vertices[j])
        glEnd()

        glPopMatrix()

class EntireCube():
    def __init__(self, N, scale):
        self.N = N
        cr = range(self.N)
        self.cubes = [Cube((x, y, z), self.N, scale) for x in cr for y in cr for z in cr]

    def mainloop(self, cubeletmap):

        rot_cube_map  = { K_UP: (-1, 0), K_DOWN: (1, 0), K_LEFT: (0, -1), K_RIGHT: (0, 1)}
        rot_slice_map = {
            K_1: (0, 0, 1), K_2: (1, 0, 1), K_3: (2, 0, 1), K_4: (0, 2, -1), K_5: (1, 2, -1),
            K_6: (2, 2, -1),
            K_F1: (0, 0, -1), K_F2: (1, 0, -1), K_F3: (2, 0, -1), K_F4: (0, 2, 1), K_F5: (1, 2, 1),
            K_F6: (2, 2, 1)
        }
        display = (1920, 1080)
        ang_x, ang_y, rot_cube = 0, 0, (0, 0)
        animate, animate_ang, animate_speed = False, 0, 5
        action = (0, 0, 0)
        solve = 0
        x = 0
        shot = 0
        rotationconstant = 0
        rotations = 1
        runtrue = 1
        f = open("123.txt", "r")
        if f.mode == 'r':
            moves = f.read()

        fair = 1
        while runtrue == 1:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == KEYDOWN:
                    if event.key == K_s:
                        solve = 1
                    if event.key in rot_cube_map:
                        rot_cube = rot_cube_map[event.key]
                if event.type == KEYDOWN:
                    if event.key in rot_cube_map:
                        rot_cube = rot_cube_map[event.key]
                    if not animate and event.key in rot_slice_map:
                        animate, action = True, rot_slice_map[event.key]
                if event.type == KEYUP:
                    if event.key in rot_cube_map:
                        rot_cube = (0, 0)


            #rot_cube = (1, 1,1)



            if (x < int((len(moves) - 5) / 3)):
                if not animate:
                    if (rotationconstant == 1):
                        animate, action = True, rot_slice_map[movement]
                        rotationconstant = 0
                    else:
                        movement, rotations = audio.run(moves, x, 1)
                        rotationconstant = rotations - 1
                        x = x+1
                        animate, action = True, rot_slice_map[movement]
            else:
                runtrue = 0





            ang_x += rot_cube[0]*2
            ang_y += rot_cube[1]*2

            glMatrixMode(GL_MODELVIEW)
            glLoadIdentity()
            glTranslatef(0, 0, -40)
            glRotatef(ang_y, 0, 1, 0)
            glRotatef(ang_x, 1, 0, 0)

            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)



            if animate:
                if animate_ang >= 90:
                    for cube in self.cubes:
                        cube.update(*action)
                    animate, animate_ang = False, 0

            k = 0
            for cube in self.cubes:
                cube.draw(colors, surfaces, vertices, animate, animate_ang, *action, k, cubeletmap)
                k = k+1
            if animate:
                animate_ang += animate_speed

            #buf = glReadPixels(260, 260, 80,80, GL_RGB, GL_BYTE)
            #bufarray[shot] = buf
            #shot = shot + 1
            #print(buf[20][20])
            #print("buf")
            #buf[y][x]
            #print(shot)
            pygame.display.flip()
            pygame.time.wait(10)

def main(cubeletmap):

    pygame.init()
    display = (640,640)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    glEnable(GL_DEPTH_TEST)

    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0]/display[1]), 0.1, 100)
    glTranslatef(0, 0, -40)
    NewEntireCube = EntireCube(3, 1.5)
    NewEntireCube.mainloop(cubeletmap)
    print("lol")
    return (bufarray)

if __name__ == '__main__':
    main()
    pygame.quit()
    quit()