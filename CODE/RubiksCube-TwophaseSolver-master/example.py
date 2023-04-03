# ############################ Examples how to use the cube solver #####################################################

import destrou as dest
import OrganiseCube as org

def run():




    a = 0
    a = dest.run()






  # cube definition string of cube we want to solve
cubestring = 'DUUBULDBFRBFRRULLLBRDFFFBLURDBFDFDRFRULBLUFDURRBLBDUDL'
cubestring = ['R', 'R', 'R', 'U', 'U', 'U', 'U', 'U', 'U', 'D', 'D', 'D', 'R', 'R', 'R', 'R', 'R', 'R', 'L', 'D',
                  'D', 'L', 'D', 'D', 'L', 'D', 'D', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'L', 'L', 'U', 'L',
                  'L', 'U', 'L', 'L', 'U', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']
#cubestring = ['U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'D', 'D',
 #                 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'L', 'L', 'L', 'L',
 #                 'L', 'L', 'L', 'L', 'L', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']

print(cubestring)
# See module enums.py for the format of the cube definition string

# ######################### Method 1: directly call the solve routine# #################################################
# Advantage: No network layer needed. Disadvantage: Only local usage possible.                                                                  #
########################################################################################################################
#RRRUUUUUURRDRRDRRDFFFFFFFFFDDDDDDLLLULLULLULLBBBBBBBBB
#  Uncomment this part if you want to use method 1
cubestringd = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for x in range(9):
    cubestringholdd = cubestring[18 + x]
    cubestringholdf = cubestring[27 + x]
    cubestringd[8-x] = cubestringholdd
    cubestring[18 + x] = cubestringholdf
for x in range(9):
    cubestring[27 + x] = cubestringd[x]

print(cubestringd)
cubestring = org.organise(cubestring)
print(cubestring)
import solver as sv
a = sv.solve(cubestring, 20, 2)  # solve with a maximum of 20 moves and a timeout of 2 seconds for example
print(a)
f= open("123.txt","w+")
f.write(a)
f.close()
#a = sv.solve(cubestring, 18, 5)  # solve with a maximum of 18 moves and a timeout of 5 seconds for example
#print(a)
#f= open("345.txt","w+")
#f.write(a)
#f.close()


    #x = 0
    #while (x < int((len(a) - 5) / 3)):
    #    audio.run(a, x, 0)







########################################################################################################################


# ############################### Method 2 a/b: Start the cubesolving-server# ##########################################
# Advantage: Tables have to be loaded only once when the server starts. Disadvantage: Network layer must be present.   #
########################################################################################################################

#----------------------------------------------------------------------------------------------------------------------
# Method 2a: Start the server from inside a Python script:
import start_server
from threading import Thread
background_thread = Thread(target=start_server.start, args=(8080, 20, 2))
background_thread.start()
# Server listens now on port 8080, maxlength 20 moves, timeout 2 seconds
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# Method 2b: Start the server from a terminal with parameters for port, maxlength and timeout:
# python start_server.py 8080 20 2
# ----------------------------------------------------------------------------------------------------------------------


# Once the server is started you can transfer the cube definition string to the server with different methods:

# ----------------------------------------------------------------------------------------------------------------------
# 1. With a webbrowser, if the server runs on the same machine on port 8080
# http://localhost:8080/DUUBULDBFRBFRRULLLBRDFFFBLURDBFDFDRFRULBLUFDURRBLBDUDL
# With a webbrowser, if the server runs on server myserver.com, port 8081
# http://myserver.com:8081/DUUBULDBFRBFRRULLLBRDFFFBLURDBFDFDRFRULBLUFDURRBLBDUDL
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# 2. With netcat, if the server runs on the same machine on port 8080
# echo DUUBULDBFRBFRRULLLBRDFFFBLURDBFDFDRFRULBLUFDURRBLBDUDL | nc localhost 8080
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# 3. With this little graphical interface.
# From within a Python script start the interface with

import client_gui


# From a terminal start the interface with
# python client_gui.py
# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
# Computer vision

# Start the interface, the server and the webcam from a terminal with

# python computer_vision.py

# ----------------------------------------------------------------------------------------------------------------------
########################################################################################################################
