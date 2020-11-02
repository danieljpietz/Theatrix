from GUI.Widgets.Fixture import *
from GUI.Widgets.Functions import *
from GUI.Widgets.Inputs import *

Bricktionary = {
    "Fixture": Fixture,
    "Value": BrickConst,
    "Multiply": BrickMult,
    "Add": BrickAdd,
    "Sine": BrickSine,
    "Cosine": BrickCos,
    "Max": BrickMax,
    "Min": BrickMin,
    "Time": BrickTime
}


def addToBricktionary(brickClass, name):
    Bricktionary[name] = brickClass

# Bricktionary.update({v: k for k, v in Bricktionary.items()})
