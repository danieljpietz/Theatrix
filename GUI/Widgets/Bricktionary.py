from GUI.Widgets.Functions import *
from GUI.Widgets.Inputs import *
from GUI.Widgets.Fixture import *

Bricktionary = {
    "Fixture": Fixture,
    "Sine": BrickSine,
    "Time": BrickTime
}

Bricktionary.update({v: k for k, v in Bricktionary.items()})

print(Bricktionary)