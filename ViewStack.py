from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from CommonGUIComponents import *
from db.helpers import *
from ViewCard import *
from ViewVideo import *
from PlaySound import *


class ViewStack(QWidget):

    def __init__(self, mainMenu=None, stackID=None,
                    pos = QPoint(300, 300), size = QSize(250, 150)):
        self.stackID = stackID
        self.mainMenu = mainMenu
        self.cardID = None
        self.viewQuestion = True
        self.index = 0
        self.count = 0

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

    def onViewVideoClick(self):
        if (self.videoLocation != ''):
            self.vv = ViewVideo(self.videoLocation)
            self.vv.create()
            print('Opening Video')
        else:
            msg = QMessageBox()
            msg.setText("No video found")
            msg.setWindowTitle("Attention!")
            retval = msg.exec_()

    @pyqtSlot()
    def onFlipClick(self):
        self.viewQuestion = not self.viewQuestion
        QWidget().setLayout(self.layout())
        self.create()

    def onNextClick(self):
        if (self.index < self.count - 1):
            self.index += 1
            self.viewQuestion = True
            QWidget().setLayout(self.layout())
            self.create()
        else:
            msg = QMessageBox()
            msg.setText("No Next")
            msg.setWindowTitle("Attention!")
            retval = msg.exec_()


    def onPreviousClick(self):
        if (self.index > 0):
            self.index -= 1
            self.viewQuestion = True
            QWidget().setLayout(self.layout())
            self.create()
        else:
            msg = QMessageBox()
            msg.setText("No Previous")
            msg.setWindowTitle("Attention!")
            retval = msg.exec_()

    def switchToCard(self, cardID):
    	#gets information from a card, same as EditStack
        self.cardID = cardID
        cardAssets = get_card_assets(self.cardID)

        #key is asset type
        #value is (id, content, filename)
        self.assetDict = {row[1]: (row[0], row[2], row[3],) for row in cardAssets}

        self.imageLocation = self.assetDict.get('image', ('', '', ''))[2]
        self.videoLocation = self.assetDict.get('video', ('', '', ''))[2]
        self.audioLocation = self.assetDict.get('audio', ('', '', ''))[2]


    def create(self):

        update_stack_review_date(self.stackID)
        self.count = 0

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
<<<<<<< HEAD
=======
        flip.clicked.connect(self.onFlipClick)
>>>>>>> 512fa2d6914bf93369a99623c4f1b97b3e2a49ae
        row.addWidget(flip)

        row.addStretch(1)

        #create button for main menu
        #button will be fixed against right and top
        back = QPushButton('Edit')
        back.clicked.connect(self.enterEditMode)
        row.addWidget(back)

        #retrieve cards from DB
        self.cardIDs = get_stack_cards(self.stackID)

        if len(self.cardIDs) > 0:
            self.switchToCard(self.cardIDs[self.index][0])
            for i in self.cardIDs:
                self.count += 1
                
        #add row for navigation
        self.fullLayout.addLayout(row)

        self.fullLayout.addStretch(1)

        if len(self.cardIDs) > 0:

            row = QHBoxLayout()

            viewCard = ViewCard(self.cardID, self.viewQuestion)
            row.addWidget(viewCard)

            self.fullLayout.addLayout(row)
            self.fullLayout.addStretch(1)

            row = QHBoxLayout()

            #next and previous buttons
            goPrevious = QPushButton('Previous')
            goPrevious.clicked.connect(self.onPreviousClick)
            row.addWidget(goPrevious)

            goNext = QPushButton('Next')
            goNext.clicked.connect(self.onNextClick)
            row.addWidget(goNext)

            row.addStretch(5)

            #TODO: add view stack code

            row.addStretch(1)
            #image
            viewImage = QPushButton('View Image')
            row.addWidget(viewImage)

            #audio
            hearAudio = PlaySound(self.audioLocation)
            row.addWidget(hearAudio)

	        #video
            viewVideo = QPushButton('View Video')
            viewVideo.clicked.connect(self.onViewVideoClick)
            row.addWidget(viewVideo)
        else:
            row = QHBoxLayout()

            noCardLabel = QLabel('There are no cards in this stack')
            row.addWidget(noCardLabel)


        self.fullLayout.addLayout(row)

        self.setLayout(self.fullLayout)

        self.show()

    #the MainMenu needs to be opened on close
    def closeEvent(self, event):
        openMainMenu(self)
        event.accept()
