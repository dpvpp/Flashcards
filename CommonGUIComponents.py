from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

#NOTE: all of the fucnction in this file are used for moving windows around
# so that they match the previous position and size of the closed window
# this should be implemented as a single window with multiple views

#takes the current window and if it has a main menu
#it will move it to the position of the current window
#with the same size and show it
def openMainMenu(curWindow):
    if curWindow.mainMenu is not None:
        curWindow.mainMenu.refresh()
        move(curWindow, curWindow.mainMenu)

def openEditWindow(curWindow):
    #NOTE: needs to imported like this because
    #of circular dependencies
    import EditStack
    curWindow.mainMenu.es = EditStack.EditStack(curWindow.mainMenu,
            curWindow.stackID, curWindow.pos(), curWindow.size())
    curWindow.mainMenu.es.create()

def openViewWindow(curWindow):
    #NOTE: needs to imported like this because
    #of circular dependencies
    import ViewStack
    curWindow.mainMenu.vs = ViewStack.ViewStack(curWindow.mainMenu,
            curWindow.stackID, curWindow.pos(), curWindow.size())
    curWindow.mainMenu.vs.create()

def move(curWindow, nextWindow):
    #copy size and position over to new window
    nextWindow.move(curWindow.pos())
    nextWindow.resize(curWindow.size())

    #show next window
    nextWindow.show()
