from GUI.Widgets.Brick import *

import numpy as np

class BrickSine(Brick):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bannerColor = [255,0,127, 255]
        self.penColor = [0,0,0,0]
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
        self.bannerColor = [255,0,127, 255]
        self.penColor = [0,0,0,0]
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
        self.bannerColor = [255,0,127, 255]
        self.penColor = [0,0,0,0]
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
        self.bannerColor = [255,0,127, 255]
        self.penColor = [0,0,0,0]
        self.initWidth = 140
        self.width = 140
        self.setTitle("min(x,y)")
        self.setInputs(['x', 'y'])
        self.setOutputs(['min(x,y)'])
        self.addPorts()

    def eval(self):
        self.outputPorts[0].value = np.min([self.inputPorts[0].getValue(), self.inputPorts[1].getValue()])