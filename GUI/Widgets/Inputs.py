from GUI.Widgets.Brick import *

class BrickTime(Brick):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bannerColor = [255,0,0, 255]
        self.penColor = [0,0,0,0]
        self.initWidth = 100
        self.width = 100
        self.setTitle("Time")
        self.setOutputs(['Time'])
        self.addPorts()
        print(self.inputPorts)