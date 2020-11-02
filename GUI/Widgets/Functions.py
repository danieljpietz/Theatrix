import numpy as np
from PyQt5.QtWidgets import QLineEdit

from GUI.Widgets.Brick import *


class BrickSine(Brick):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bannerColor = [255, 0, 127, 255]
        self.penColor = [0, 0, 0, 0]
        self.initWidth = 140
        self.width = 140
        self.setTitle("sin(x)")
        self.setInputs(['x'])
        self.setOutputs(['sin(x)'])
        self.addPorts()

    def eval(self):
        self.outputPorts[0].value = np.sin(self.inputPorts[0].getValue())


class BrickCos(Brick):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bannerColor = [255, 0, 127, 255]
        self.penColor = [0, 0, 0, 0]
        self.initWidth = 140
        self.width = 140
        self.setTitle("cos(x)")
        self.setInputs(['x'])
        self.setOutputs(['cos(x)'])
        self.addPorts()

    def eval(self):
        self.outputPorts[0].value = np.cos(self.inputPorts[0].getValue())


class BrickMax(Brick):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bannerColor = [255, 0, 127, 255]
        self.penColor = [0, 0, 0, 0]
        self.initWidth = 140
        self.width = 140
        self.setTitle("max(x,y)")
        self.setInputs(['x', 'y'])
        self.setOutputs(['max(x,y)'])
        self.addPorts()

    def eval(self):
        self.outputPorts[0].value = np.max([self.inputPorts[0].getValue(), self.inputPorts[1].getValue()])


class BrickMin(Brick):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bannerColor = [255, 0, 127, 255]
        self.penColor = [0, 0, 0, 0]
        self.initWidth = 140
        self.width = 140
        self.setTitle("min(x,y)")
        self.setInputs(['x', 'y'])
        self.setOutputs(['min(x,y)'])
        self.addPorts()

    def eval(self):
        self.outputPorts[0].value = np.min([self.inputPorts[0].getValue(), self.inputPorts[1].getValue()])


class BrickMult(Brick):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bannerColor = [255, 0, 127, 255]
        self.penColor = [0, 0, 0, 0]
        self.initWidth = 140
        self.width = 140
        self.setTitle("multiply(x,y)")
        self.setInputs(['x', 'y'])
        self.setOutputs(['multiply(x,y)'])
        self.addPorts()

    def eval(self):
        self.outputPorts[0].value = self.inputPorts[0].getValue() * self.inputPorts[1].getValue()


class BrickAdd(Brick):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bannerColor = [255, 0, 127, 255]
        self.penColor = [0, 0, 0, 0]
        self.initWidth = 140
        self.width = 140
        self.setTitle("add(x,y)")
        self.setInputs(['x', 'y'])
        self.setOutputs(['add(x,y)'])
        self.addPorts()

    def eval(self):
        self.outputPorts[0].value = self.inputPorts[0].getValue() + self.inputPorts[1].getValue()


class BrickConst(Brick):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bannerColor = [255, 0, 127, 255]
        self.penColor = [0, 0, 0, 0]
        self.initWidth = 140
        self.width = 140
        self.setTitle("Value")
        self.setInputs([])
        self.setOutputs(['Value'])
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(self.width - 40, 30)
        self.textbox.setStyleSheet("color: rgb(255, 255, 255);")
        self.textbox.setParent(self)
        self.addPorts()

    def eval(self):
        try:
            self.outputPorts[0].value = float(self.textbox.text())
        except:
            self.outputPorts[0].value = 0
