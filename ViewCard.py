from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from CommonGUIComponents import *
from db.helpers import *

class ViewCard(QWidget):

    def __init__(self, cardID, viewQuestion=True, fullDisplay=True):
        self.cardID = cardID
        self.viewQuestion = viewQuestion
        self.fullDisplay = fullDisplay

        super().__init__()


        if self.fullDisplay:
            self.setMaximumSize(300, 200)
            self.setMinimumSize(300, 200)
        else:
            self.setMaximumSize(150, 100)
            self.setMinimumSize(150, 100)

        self.setStyleSheet("background-color: rgb(255,255,255)")

        self.layout = QVBoxLayout(self)

        cardAssets = get_card_assets(self.cardID)
        assetDict = {row[1]: (row[0], row[2], row[3],) for row in cardAssets}

        question = assetDict.get('question', ('', '', ''))[1]
        answer = assetDict.get('answer', ('', '', ''))[1]

        text = question if self.viewQuestion else answer

        self.textLabel = QLabel(text)
        self.textLabel.setAlignment(Qt.AlignCenter)
        self.textLabel.setWordWrap(True)

        if self.fullDisplay:
            self.textLabel.setStyleSheet("font: 12px")
        else:
            self.textLabel.setStyleSheet("font: 6px")

        self.layout.addWidget(self.textLabel)

        self.setLayout(self.layout)

