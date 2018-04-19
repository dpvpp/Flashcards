import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from pathlib import Path #for checking file exist

class PlaySound(QWidget):

    # wav is the file path
    def __init__(self, wav):

        super().__init__()

        #check if file exist
        my_file = Path(wav)

        if my_file.is_file():
            self.fileExists = True
        else:
            self.fileExists = False
            print('file NOT exist')

        self.wav_path = wav

        self.initUI()

    def initUI(self):
        self.setMinimumSize(32,32)

        self.b1 = QPushButton("Play", self)
        self.b1.clicked.connect(self.play)

    def play(self):
        QSound.play(self.wav_path)
