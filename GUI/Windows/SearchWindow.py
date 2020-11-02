import numpy as np
from PyQt5.QtWidgets import QWidget, QScrollArea, QVBoxLayout

from GUI.Widgets.Bricktionary import *
from GUI.Widgets.SearchListEntry import *


class SearchWindow(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bannerColor = [127, 127, 127, 127]
        self.brushColor = [10, 10, 10, 200]
        self.initWidth = 400
        self.initHeight = 400
        self.width = self.initWidth
        self.height = self.initHeight
        self.resize(self.width, self.height)
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(self.width - 40, 30)
        self.textbox.setStyleSheet("color: rgb(255, 255, 255);")
        self.scroll = QScrollArea()  # Scroll Area which contains the widgets, set as the centralWidget
        self.widget = QWidget()  # Widget that contains the collection of Vertical Box
        self.vbox = QVBoxLayout()  # The Vertical Box that contains the Horizontal Boxes of  labels and buttons
        self.mainWindow = []
        self.objects = []

        for brick in Bricktionary:
            if type(brick) != str:
                break
            entry = SearchListEntry(brick)
            self.objects.append(entry)
            self.vbox.addWidget(entry)
            entry.setParent(self.widget)
            entry.show()

        self.widget.setLayout(self.vbox)
        # Scroll Area Properties
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)
        self.scroll.setParent(self)
        self.scroll.move(20, 70)
        self.scroll.resize(self.width - 40, self.height - 70 - 20)
        self.scroll.show()

    def paintEvent(self, event):
        penColor = [200, 200, 200, 200]
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing);
        painter.setPen(QPen(QColor(penColor[0], penColor[1], penColor[2], penColor[3]), 2, Qt.SolidLine))
        gradient = QLinearGradient(0, 0, 0, self.height)
        gradient.setColorAt(0.0,
                            QColor(self.bannerColor[0], self.bannerColor[1], self.bannerColor[2], self.bannerColor[3]))
        gradient.setColorAt(0.15,
                            QColor(self.brushColor[0], self.brushColor[1], self.brushColor[2], self.brushColor[3]))
        painter.setBrush(QBrush(QColor(self.brushColor[0], self.brushColor[1], self.brushColor[2], self.brushColor[3]),
                                Qt.SolidPattern))
        # painter.setBrush(QBrush(gradient))
        painter.drawRoundedRect(0, 0, self.width, self.height, np.sqrt(self.width), np.sqrt(self.height))

    def mousePressEvent(self, event):
        self.lastTouch = event.pos()
        self.position = self.pos()
        pass

    def mouseMoveEvent(self, event):
        self.move(self.pos() + event.pos() - self.lastTouch)
