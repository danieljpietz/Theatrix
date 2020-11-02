from PyQt5 import QtCore
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import QPoint
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QBrush, QPen, QColor, QLinearGradient
from PyQt5.QtWidgets import QLabel

from GUI.Widgets.Bricktionary import Bricktionary


class SearchListEntry(QtWidgets.QWidget):
    """
    Custom Qt Widget to show a power bar and dial.
    Demonstrating compound and custom-drawn widget.

    Left-clicking the button shows the color-chooser, while
    right-clicking resets the color to None (no-color).
    """

    colorChanged = QtCore.pyqtSignal()

    def __init__(self, itemName, *args, **kwargs):
        super().__init__(*args, **kwargs)
        layout = QtWidgets.QVBoxLayout()
        self.height = 20
        self.width = 330
        self.itemName = itemName
        self.item = QLabel(itemName)
        self.item.move(10, 0)
        self.item.setStyleSheet("color: rgb(255, 255, 255); background-color: rgba(0,0,0,0);")
        itemFont = QtGui.QFont()
        itemFont.setBold(True)
        self.item.setFont(itemFont)
        self.item.adjustSize()
        self.item.setParent(self)
        self.item.show()
        self.setLayout(layout)

    def mouseDoubleClickEvent(self, event):
        window = self.parent().parent().parent().parent().parent()
        window.addBrick(Bricktionary[self.itemName], self.mapTo(window, QPoint(0, 0)))
        window.hideSearchWindow()

    def paintEvent(self, event):
        painter = QPainter(self)
        self.bannerColor = [255, 255, 255, 255]
        self.brushColor = [255, 255, 255, 20]
        self.penColor = [255, 255, 255, 255]
        gradient = QLinearGradient(0, 0, self.width, 0)
        gradient.setColorAt(0.0,
                            QColor(self.bannerColor[0], self.bannerColor[1], self.bannerColor[2], self.bannerColor[3]))
        gradient.setColorAt(0.85,
                            QColor(self.brushColor[0], self.brushColor[1], self.brushColor[2], self.brushColor[3]))
        painter.setBrush(QBrush(QColor(self.brushColor[0], self.brushColor[1], self.brushColor[2], self.brushColor[3]),
                                Qt.SolidPattern))
        painter.setPen(
            QPen(QColor(self.penColor[0], self.penColor[1], self.penColor[2], self.penColor[3]), 2, Qt.SolidLine))
        painter.drawRect(0, 0, self.width, self.height)


"""
class SearchListEntry(QtWidgets.QWidget):
    def __init__(self, steps = 0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.height = 20
        self.width = 200
        self.resize(self.width,self.height)
        self.label = QLabel("T")
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setParent(self)
        self.label.show()

    def sizeHint(self):
        return QtCore.QSize(self.width, self.height)
    def paintEvent(self, event):
        print("Here")
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 5, Qt.DotLine))
        painter.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
        painter.drawRect(0, 0, self.width, self.height)
"""
