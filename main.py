import sys
from GUI.Windows.windows import *
from PyQt5.QtWidgets import QApplication
from DMX.UpdateHandler import *

def main():
    App = QApplication(sys.argv)
    updateHandler = UpdateHandler()
    window = MainWindow()
    updateHandler.window = window
    window.updateManager = updateHandler
    updateHandler.begin()
    sys.exit(App.exec())
    updateHandler.updateThread.join()

if __name__ == '__main__':
    main()
