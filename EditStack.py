from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from CommonGUIComponents import *

class EditStack(QWidget):

    def __init__(self, mainMenu=None, stackID=None,
                    pos = QPoint(300, 300), size = QSize(250, 150)):
        self.stackID = stackID
        self.mainMenu = mainMenu
        self.unsavedChanges = False

        super().__init__()

        #set size and position
        #usually passed in by constructor from
        #the main menu
        self.move(pos)
        self.resize(size)

        self.setWindowTitle('Edit Stack')

    @pyqtSlot()
    def backToMainMenu(self):
        if not self.checkSaved():
            return
        self.hide()
        openMainMenu(self)

    @pyqtSlot()
    def enterStudyMode(self):
        if not self.checkSaved():
            return
        self.hide()
        openViewWindow(self)

    def create(self):

        self.fullLayout = QVBoxLayout()

        #create the top row of the layout to have
        #a main menu button and a study button

        row = QHBoxLayout()

        #create button for main menu
        #button will be fixed against left and top
        back = QPushButton('Main Menu')
        back.clicked.connect(self.backToMainMenu)
        row.addWidget(back)

        row.addStretch(1)

        #create button for new card
        newcard = QPushButton('Add Card')

        row.addWidget(newcard)

        row.addStretch(1)

        #create button for main menu
        #button will be fixed against right and top
        back = QPushButton('Study')
        back.clicked.connect(self.enterStudyMode)
        row.addWidget(back)

        self.fullLayout.addLayout(row)

        self.fullLayout.addStretch(1)

        #rest of GUI added here

        row = QHBoxLayout()

        #TODO: list of cards

        row.addStretch(2)

        editSplit = QVBoxLayout()

        editArea = QGroupBox('Edit Card')

        #this could potentially be dynamically generated
        #it would be challenging to handle the updates

        editForm = QFormLayout()

        self.frontText = QTextEdit()
        self.frontText.textChanged.connect(self.makeChanges)
        editForm.addRow(QLabel('Front text'), self.frontText)

        self.backText = QTextEdit()
        self.backText.textChanged.connect(self.makeChanges)
        editForm.addRow(QLabel('Back text'), self.backText)

        #TODO: file browser for selecting an image

        editArea.setLayout(editForm)

        editSplit.addWidget(editArea)

        saveChangesDialog = QDialogButtonBox(QDialogButtonBox.Save | QDialogButtonBox.Discard)
        saveChangesDialog.accepted.connect(self.save)
        saveChangesDialog.rejected.connect(self.reject)

        editSplit.addWidget(saveChangesDialog)

        editSplit.addStretch(1)

        #TODO: add drag/drop components (maybe)
        #could be something else

        row.addLayout(editSplit)

        row.addStretch(1)

        self.fullLayout.addLayout(row)

        self.fullLayout.addStretch(1)

        self.setLayout(self.fullLayout)


        self.show()

    #save changes to database
    def save(self):
        #TODO: save to datbase
        self.unsavedChanges = False

    def reject(self):
        #TODO: reload data from database
        self.unsavedChanges = False

    #sets the unsavedChanges flag
    #a method is needed because assignment isn't allowed inside of lambda
    #this method is called whenever the textboxes are modified
    @pyqtSlot()
    def makeChanges(self):
        self.unsavedChanges = True

    #check if the content has been saved
    #and save it if the user choses to
    #returns whether it is OK to exit
    def checkSaved(self):
        if self.unsavedChanges:
            reply = QMessageBox.question(self, 'Unsaved changes',
                'Would you like to save your changes?',
                 QMessageBox.Save | QMessageBox.No | QMessageBox.Cancel,
                 QMessageBox.Save)
            if reply == QMessageBox.Save:
                self.save()
            elif reply == QMessageBox.Cancel:
                return False

        return True


    #the MainMenu needs to be opened on close
    #edits need to be checked to unsure nothing is unsaved
    def closeEvent(self, event):
        close = True

        if not self.checkSaved():
            event.ignore()
            return

        openMainMenu(self)
        event.accept()
