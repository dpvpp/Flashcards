from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap
from db.helpers import *
import sys

class ImagePreview(QWidget):

    def __init__(self, imagePath, size):
        super().__init__()
        self.imagePath = imagePath
        self.size = size
        self.initUI()

    def initUI(self):
        self.setMinimumSize(self.size,self.size)
        label = QLabel(self)

        if self.imagePath is None:
            pixmap = QPixmap('No_image.png')
        elif self.imagePath[3] is None:
            pixmap = QPixmap('No_image.png')
        else:
            pixmap = QPixmap(self.imagePath[3])

        resize_pixmap = pixmap.scaled(self.size, self.size)
        label.setPixmap(resize_pixmap)
