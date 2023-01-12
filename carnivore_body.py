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
            self.jaugeFaim = random.randint(70, 80)
            self.jaugeFatigue = random.randint(50, 60)
            self.jaugeReproduction = random.randint(20, 30)
            self.esperance = random.randint(500, 600)
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

    def show(self):
        core.Draw.circle((163, 46, 46), self.position, self.size)
        super().show()

    def update(self):
        super().update()
