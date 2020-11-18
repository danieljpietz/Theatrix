import numpy as np

from GUI.Widgets.Brick import *


class Fixture(Brick):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bannerColor = [255, 0, 0, 255]
        self.penColor = [0, 0, 0, 0]
        self.width = 100
        self.setTitle("Fixture")
        self.setInputs(['Pan', 'Tilt', 'Red', 'Green', 'Blue', 'Dimmer', 'Shutter', 'Address'])
        self.addPorts()
        self.isOutput = True

    def eval(self):
        if self.inputPorts[7].isConnected:
            portVal = int(self.inputPorts[7].getValue())
            adr = portVal
        else:
            adr = 0

        # Evaluate Pan
        if self.inputPorts[0].isConnected:
            portVal = self.inputPorts[0].getValue()
            portVal = portVal * (portVal > 0) * (portVal <= 1) + (portVal > 1)
            panHigh = np.floor(255 * portVal)
            panLow = np.floor(255 * (255 * portVal - panHigh))
            self.parentWindow.updateManager.port.dmx_frame[adr + 0] = int(panHigh)
            self.parentWindow.updateManager.port.dmx_frame[adr + 1] = int(panLow)
        else:
            self.parentWindow.updateManager.port.dmx_frame[adr + 0] = 0
            self.parentWindow.updateManager.port.dmx_frame[adr + 1] = 0

        if self.inputPorts[1].isConnected:
            portVal = self.inputPorts[1].getValue()
            portVal = portVal * (portVal > 0) * (portVal <= 1) + (portVal > 1)
            tiltHigh = np.floor(255 * portVal)
            tiltLow = np.floor(255 * (255 * portVal - tiltHigh))
            self.parentWindow.updateManager.port.dmx_frame[adr + 2] = int(tiltHigh)
            self.parentWindow.updateManager.port.dmx_frame[adr + 3] = int(tiltLow)
        else:
            self.parentWindow.updateManager.port.dmx_frame[adr + 2] = 0
            self.parentWindow.updateManager.port.dmx_frame[adr + 3] = 0

        if self.inputPorts[6].isConnected:
            self.parentWindow.updateManager.port.dmx_frame[adr + 7] = int(self.inputPorts[6].getValue())
        else:
            self.parentWindow.updateManager.port.dmx_frame[adr + 7] = 24

        redVal = 0
        blueVal = 0
        greenVal = 0
        dimmerVal = 1
        if self.inputPorts[2].isConnected:
            redVal = max([self.inputPorts[2].getValue(), 0])
            redVal = redVal * (redVal <= 1) + (redVal > 1)
        if self.inputPorts[3].isConnected:
            greenVal = max([self.inputPorts[3].getValue(), 0])
            greenVal = greenVal * (greenVal <= 1) + (greenVal > 1)
        if self.inputPorts[4].isConnected:
            blueVal = max([self.inputPorts[4].getValue(), 0])
            blueVal = blueVal * (blueVal <= 1) + (blueVal > 1)
        if self.inputPorts[5].isConnected:
            dimmerVal = max([self.inputPorts[5].getValue(), 0])
            dimmerVal = dimmerVal * (dimmerVal <= 1) + (dimmerVal > 1)


        whiteVal = min([redVal, blueVal, greenVal])
        redVal = redVal - whiteVal
        blueVal = blueVal - whiteVal
        greenVal = greenVal - whiteVal

        portVal = redVal
        portHigh = np.floor(255 * portVal)
        portLow = np.floor(255 * (255 * portVal - portHigh))
        self.parentWindow.updateManager.port.dmx_frame[adr + 8] = int(portHigh)
        self.parentWindow.updateManager.port.dmx_frame[adr + 9] = int(portLow)

        portVal = greenVal
        portHigh = np.floor(255 * portVal)
        portLow = np.floor(255 * (255 * portVal - portHigh))
        self.parentWindow.updateManager.port.dmx_frame[adr + 10] = int(portHigh)
        self.parentWindow.updateManager.port.dmx_frame[adr + 11] = int(portLow)

        portVal = blueVal
        portHigh = np.floor(255 * portVal)
        portLow = np.floor(255 * (255 * portVal - portHigh))
        self.parentWindow.updateManager.port.dmx_frame[adr + 12] = int(portHigh)
        self.parentWindow.updateManager.port.dmx_frame[adr + 13] = int(portLow)

        portVal = whiteVal
        portHigh = np.floor(255 * portVal)
        portLow = np.floor(255 * (255 * portVal - portHigh))
        self.parentWindow.updateManager.port.dmx_frame[adr + 14] = int(portHigh)
        self.parentWindow.updateManager.port.dmx_frame[adr + 15] = int(portLow)

        portVal = dimmerVal
        portHigh = np.floor(255 * portVal)
        portLow = np.floor(255 * (255 * portVal - portHigh))
        self.parentWindow.updateManager.port.dmx_frame[adr + 5] = int(portHigh)
        self.parentWindow.updateManager.port.dmx_frame[adr + 6] = int(portLow)

        """
        for port in self.inputPorts:
            if port.isConnected:
                print(port.getValue())
        """
