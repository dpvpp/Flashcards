from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from db.helpers import *
from ImagePreview import *
from ViewStack import *
from EditStack import *


class MainMenu(QWidget):

    def __init__(self):

        super().__init__()

        #create main window
        #left, top, width, height
        self.setGeometry(300, 300, 750, 450)
        self.setWindowTitle('Main Menu')


    @pyqtSlot()
    def onStudyClick(self, stackID):
        #hide the current window
        self.hide()

        #clear out the edit window
        self.es = None

        #create the view window
        self.vs = ViewStack(self, stackID, self.pos(), self.size())
        self.vs.create()
        print('Studying Stack ' + str(stackID))

    @pyqtSlot()
    def onEditClick(self, stackID):
        #hide the current window
        self.hide()

        #clear out the previous view window
        self.vs = None

        #create the edit window
        self.es = EditStack(self, stackID, self.pos(), self.size())
        self.es.create()
        print('Editing Stack ' + str(stackID))

    @pyqtSlot()
    def onDeleteClick(self, stackID):
        print('Deleting Stack ' + str(stackID))
        delete_stack(stackID)

        self.refresh()

    @pyqtSlot()
    def onAddStackClick(self):
        print('Adding Stack')

        #create dialog box with text input for the
        #name of the stack
        stackName, okPressed = QInputDialog.getText(self,
                            'Add Stack',
                            'Enter name for new stack',
                            QLineEdit.Normal, '')

        #if the ok button was pressed create the new stack
        #will be false if cancel button is pressed or the
        #dialog is closed
        if okPressed:
            print('New Stack: ' + stackName)

            #check if stackname is empty or contains only whitespace
            if stackName.isspace() or stackName is '':
                return

            stackName = stackName.strip()

            #check if stackname exists already
            if stack_name_exists(stackName):
                return

            create_stack(stackName)

            self.refresh()


    def refresh(self):
        QWidget().setLayout(self.layout())
        self.create()


    def create(self):

        #keep track of buttons
        self.studyButttons = []
        self.editButtons = []
        self.deleteButtons = []

        stacks = get_stacks()

        self.fullList = QVBoxLayout()

        #layout the list of stacks
        #essentially this creates a bunch of horizontal boxes (QHBoxLayout) and
        #adds the elements for each stack to them, each of these hboxes is then
        #added to vertical box (QVBoxLayout) created above to create the overall
        #layout
        for stack in stacks:
            stackID = stack[0]
            stackName = str(stack[1])
            lastReviewed = str(stack[2])

            row = QHBoxLayout()
            row.addStretch(0.5)

            stackPreview = QVBoxLayout()
            stackPreview.setSpacing(0)

            stackNameLabel = QLabel(stackName)
            stackNameLabel.setAlignment(Qt.AlignCenter)
            stackPreview.addWidget(stackNameLabel)

            cards = get_stack_cards(stackID)
            if len(cards) > 0:
                topCard = ViewCard(cards[0][0], True, False)
                stackPreview.addWidget(topCard)

            row.addLayout(stackPreview)

            row.addStretch(1)
            lastReviewedLabel = QLabel("Last Reviewed: \n" + lastReviewed)
            row.addWidget(lastReviewedLabel)

            row.addStretch(4)

            #note: the "check" parameter is needed in the lambda as it
            #is passed by the clicked event (it is a boolean signifying if
            # the button has been checked, if checkable)

            #create study button
            study = QPushButton('Study')
            study.clicked.connect(lambda check,x=stackID: self.onStudyClick(x))
            self.studyButttons.append(study)
            row.addWidget(study)

            #create edit button
            edit = QPushButton('Edit')
            edit.clicked.connect(lambda check,x=stackID: self.onEditClick(x))
            self.editButtons.append(edit)
            row.addWidget(edit)

            #create delete button
            delete = QPushButton('Delete')
            delete.clicked.connect(lambda check,x=stackID: self.onDeleteClick(x))
            self.deleteButtons.append(delete)
            row.addWidget(delete)

            row.addStretch(1)

            self.fullList.addStretch(1)
            self.fullList.addLayout(row)

        #add button for new stack
        self.fullList.addStretch(1)
        row = QHBoxLayout()
        addNew = QPushButton('Add new stack')
        addNew.clicked.connect(self.onAddStackClick)
        row.addWidget(addNew)
        self.fullList.addLayout(row)

        #set the layout for the window to the vbox layout
        self.setLayout(self.fullList)

        self.show()
