import guiconverter as gui
import animation as animation



def rungui():

    cubeletmap = gui.run()
    solvevid = animation.main(cubeletmap)
    return solvevid

rungui()
