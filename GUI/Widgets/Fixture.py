from GUI.Widgets.Brick import *


class Fixture(Brick):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bannerColor = [255, 0, 0, 255]
        self.penColor = [0,0,0,0]
        self.width = 100
        self.setTitle("Fixture")
        self.setInputs(['Red', 'Green', 'Blue', 'Azimuth', 'Elevation'])
        self.addPorts()
        print(self.inputPorts)