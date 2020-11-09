import threading as threading
import time as tm
import os
import pyenttec as dmx


class UpdateHandler(object):
    def __init__(self):
        self.refreshRate = 80
        self.window = None
        self.shouldUpdate = True
        self.updateThread = threading.Thread(target=self.update)
        self.updateID = -1
        if os.name == 'nt':
            self.port = 0 * [512]
            pass
        else:
            self.port = dmx.select_port(0)
            pass  # other (unix)


    def begin(self):
        self.updateThread.start()

    def update(self):
        masterClock = tm.time()
        drift = 0
        while self.shouldUpdate:
            self.updateID = 1 + self.updateID
            self.window.updateDMX()
            if os.name != 'nt':
                self.port.render()
            drift = (tm.time() - masterClock) - self.updateID / self.refreshRate
            tm.sleep(1 / self.refreshRate - drift * (drift < 1 / self.refreshRate))
        pass
