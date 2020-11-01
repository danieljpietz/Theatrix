##
## This is the file for the main window
## All main window stuff goes here
##
from PyQt5 import QtGui
from PyQt5.QtGui import QPainterPath
from PyQt5.QtCore import QPoint

from GUI.Windows.SearchWindow import *


class ConnectionHandler(QWidget):
    def __init__(self, steps = 0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.inputPorts = []
        self.outputPorts = []

        pass

    def setParentWindow(self, window):
        self.window = window
        self.resize(window.size())
        self.move(0, 0)

    def addBrick(self, brick):
        for port in brick.inputPorts:
            self.inputPorts.append(port)
        for port in brick.outputPorts:
            self.outputPorts.append(port)

    def tryConnect(self, port, mousePos):
        mousePos = port.mapToGlobal(mousePos) - QPoint(self.window.size().width(), 0)
        if port.portType == "Input":
            for portNew in self.outputPorts:
                portPos = portNew.parent.mapToGlobal(portNew.pos()) - QPoint(self.window.size().width(), 0)
                if (mousePos.x() >= portPos.x()) and (mousePos.x() <= (portPos.x() + portNew.width)) and (
                        mousePos.y() >= portPos.y()) and (mousePos.y() <= (portPos.y() + portNew.height)):
                    if (port.parent != portNew.parent) and (not port.isConnectedTo(portNew)):
                        if port.isConnected:
                            port.disconnect(port.connections[0])
                        port.connections = [portNew]
                        portNew.connections.append(port)
                        port.isConnected = True
                        portNew.isConnected = True

        elif port.portType == "Output":
            for portNew in self.inputPorts:
                portPos = portNew.parent.mapToGlobal(portNew.pos()) - QPoint(self.window.size().width(), 0)
                if (mousePos.x() >= portPos.x()) and (mousePos.x() <= (portPos.x() + portNew.width)) and (
                        mousePos.y() >= portPos.y()) and (mousePos.y() <= (portPos.y() + portNew.height)):
                    if (port.parent != portNew.parent) and (not port.isConnectedTo(portNew)):
                        if portNew.isConnected:
                            portNew.disconnect(portNew.connections[0])
                        port.connections.append(portNew)
                        portNew.connections = [port]
                        port.isConnected = True
                        portNew.isConnected = True