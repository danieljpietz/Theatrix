import threading as threading
import time as tm

import pyenttec as dmx


class UpdateHandler(object):
    def __init__(self):
        self.refreshRate = 40
        self.window = None
        self.shouldUpdate = True
        self.updateThread = threading.Thread(target=self.update)
        self.updateID = -1
        self.port = dmx.select_port()

    def begin(self):
        self.updateThread.start()

    def update(self):
        masterClock = tm.time()
        drift = 0
        while self.shouldUpdate:
            self.updateID = 1 + self.updateID
            self.window.updateDMX()
            self.port.render()
            drift = (tm.time() - masterClock) - self.updateID / self.refreshRate
            tm.sleep(1 / self.refreshRate - drift * (drift < 1 / self.refreshRate))
        pass
