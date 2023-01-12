import random

from pygame import Vector2

from body import Body

import core


class CarnivoreBody(Body):
    def __init__(self, parent):
        Body.__init__(self)
        self.size = 8
        self.vitesse = Vector2()
        self.vitesseMax = random.randint(3, 4)
        self.acceleration = Vector2()
        self.accelerationMax = random.randint(4, 5)
        self.faim = 0
        self.fatigue = 0
        self.reproduction = 0
        if parent is None:
            self.jaugeFaim = random.randint(7, 8)
            self.jaugeFatigue = random.randint(5, 6)
            self.jaugeReproduction = random.randint(2, 3)
            self.esperance = random.randint(30, 40)
        else:
            evolution = random.randint(0, 2) - 1
            self.jaugeFaim = parent.body.jaugeFaim + (parent.body.jaugeFaim * evolution)
            evolution = random.randint(0, 2) - 1
            self.jaugeFatigue = parent.body.jaugeFatigue + (parent.body.jaugeFatigue * evolution)
            evolution = random.randint(0, 2) - 1
            self.jaugeReproduction = parent.body.jaugeReproduction + (parent.body.jaugeReproduction * evolution)
            evolution = random.randint(0, 2) - 1
            self.esperance = parent.body.esperance + (parent.body.esperance * evolution * 3)

        self.jaugeFaim *= core.fps
        self.jaugeFatigue *= core.fps
        self.jaugeReproduction *= core.fps
        self.esperance *= core.fps

    def show(self):
        super().show()
        core.Draw.circle((163, 46, 46), self.position, self.size)
