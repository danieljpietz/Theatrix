import sys
from GUI.Windows.windows import *
from GUI.Widgets.widgets import *
from PyQt5.QtWidgets import QApplication, QMainWindow
def main():
    App = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(App.exec())

if __name__ == '__main__':
    main()
