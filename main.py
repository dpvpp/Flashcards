#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QApplication
from MainMenu import *
from ViewStack import *
from EditStack import *

def main():
    # create db tables
    initialize_tables()

    #create the application
    application = QApplication(sys.argv)

    #testing code to open up specific window from the start
    if len(sys.argv) > 1:
        if sys.argv[1] == 'edit':
            estack = EditStack()
            estack.create()
        elif sys.argv[1] == 'view':
            vstack = ViewStack()
            vstack.create()
    else:
        menu = MainMenu()
        menu.create()

    #wait for application to exit
    exitCode = application.exec_()
    sys.exit(exitCode)


if __name__ == "__main__":
    main()
