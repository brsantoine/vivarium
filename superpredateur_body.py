import random

from pygame import Vector2

from body import Body

import core


class SuperpredateurBody(Body):
    def __init__(self, parent):
        Body.__init__(self)
        self.size = 10
        self.vitesse = Vector2()
        self.vitesseMax = random.randint(4, 5)
        self.acceleration = Vector2()
        self.accelerationMax = random.randint(5, 6)
        self.faim = 0
        self.fatigue = 0
        self.reproduction = 0
        if parent is None:
            self.jaugeFaim = random.randint(90, 100)
            self.jaugeFatigue = random.randint(60, 70)
            self.jaugeReproduction = random.randint(40, 50)
            self.esperance = random.randint(500, 600)
        else:
            evolution = random.randint(0, 2) - 1
            self.jaugeFaim = parent.body.jaugeFaim + (parent.body.jaugeFaim * evolution / 100)
            evolution = random.randint(0, 2) - 1
            self.jaugeFatigue = parent.body.jaugeFatigue + (parent.body.jaugeFatigue * evolution / 100)
            evolution = random.randint(0, 2) - 1
            self.jaugeReproduction = parent.body.jaugeReproduction + (parent.body.jaugeReproduction * evolution / 100)
            evolution = random.randint(0, 2) - 1
            self.esperance = parent.body.esperance + (parent.body.esperance * evolution * 3 / 100)

        self.jaugeFaim *= core.fps
        self.jaugeFatigue *= core.fps
        self.jaugeReproduction *= core.fps

    def show(self):
        core.Draw.circle((82, 82, 82), self.position, self.size)
        super().show()

    def update(self):
        super().update()

