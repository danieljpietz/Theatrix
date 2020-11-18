from GUI.Widgets.Fixture import *
from GUI.Widgets.Functions import *
from GUI.Widgets.Inputs import *

Bricktionary = {
    "Fixture": Fixture,
    "Value": BrickConst,
    "Multiply": BrickMult,
    "Add": BrickAdd,
    "Mod": BrickMod,
    "Sine": BrickSine,
    "Cosine": BrickCos,
    "Max": BrickMax,
    "Min": BrickMin,
    "Time": BrickTime
}

Bricktionary.update({v: k for k, v in Bricktionary.items()})

def addToBricktionary(brickClass, name):
    Bricktionary[name] = brickClass


