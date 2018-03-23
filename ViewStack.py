from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from CommonGUIComponents import *

class ViewStack(QWidget):

    def __init__(self, mainMenu=None, stackID=None,
                    pos = QPoint(300, 300), size = QSize(250, 150)):
        self.stackID = stackID
        self.mainMenu = mainMenu

        super().__init__()

        #set size and position
        #usually passed in by constructor from
        #the main menu
        self.move(pos)
        self.resize(size)

        self.setWindowTitle('View Stack')


    @pyqtSlot()
    def backToMainMenu(self):
        #switch to main menu with current size and position
        openMainMenu(self)
        self.hide()

    @pyqtSlot()
    def enterEditMode(self):
        #switch to main menu with current size and position
        openEditWindow(self)
        self.hide()

    def create(self):

        self.fullLayout = QVBoxLayout()

        #create the top row of the layout to have
        #a main menu button and a edit button

        row = QHBoxLayout()

        #create button for main menu
        #button will be fixed against left and top
        back = QPushButton('Main Menu')
        back.clicked.connect(self.backToMainMenu)
        row.addWidget(back)

        row.addStretch(1)

        #create button for flipping card
        flip = QPushButton('Flip')
        row.addWidget(flip)

        row.addStretch(1)

        #create button for main menu
        #button will be fixed against right and top
        back = QPushButton('Edit')
        back.clicked.connect(self.enterEditMode)
        row.addWidget(back)

        #add row for navigation
        self.fullLayout.addLayout(row)

        self.fullLayout.addStretch(1)

        #GUI for showing cards goes here
        #needs to be added to self.fullLayout

        #TODO: add view stack code

        self.setLayout(self.fullLayout)

        self.show()

    #the MainMenu needs to be opened on close
    def closeEvent(self, event):
        openMainMenu(self)
        event.accept()
