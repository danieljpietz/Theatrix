from GUI.Widgets.Brick import *


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
        print(self.inputPorts)