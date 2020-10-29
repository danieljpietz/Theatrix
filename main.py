import sys
from Windows.windows import *
from Widgets.widgets import *

def main():
    App = QApplication(sys.argv)
    window = MainWindow()

    sys.exit(App.exec())

if __name__ == '__main__':
    main()
