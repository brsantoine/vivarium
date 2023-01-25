import random

from pygame import Vector2

from body import Body

import core
from fustrum import Fustrum


class DecomposeurBody(Body):
    def __init__(self, parent):
        Body.__init__(self)
        params = core.memory("scenario")['Decomposeur']['parametres']
        self.fustrum = Fustrum(100, self)
        self.size = 2
        self.vitesse = Vector2()
        self.vitesseMax = random.randint(params['vitesseMax'][0], params['vitesseMax'][1])
        self.acceleration = Vector2()
        self.accelerationMax = random.randint(params['accelerationMax'][0], params['accelerationMax'][1])
        self.faim = 0
        self.fatigue = 0
        self.reproduction = 0
        if parent is None:
            self.jaugeFaim = random.randint(params['MaxFaim'][0], params['MaxFaim'][1])
            self.jaugeFatigue = random.randint(params['MaxFatigue'][0], params['MaxFatigue'][1])
            self.jaugeReproduction = random.randint(params['MaxReproduction'][0], params['MaxReproduction'][1])
            self.esperance = random.randint(params['Esperance'][0], params['Esperance'][1])
            self.jaugeFaim *= core.fps
            self.jaugeFatigue *= core.fps
            self.jaugeReproduction *= core.fps
        else:
            evolution = random.randint(0, 2) - 1
            self.jaugeFaim = parent.body.jaugeFaim + (parent.body.jaugeFaim * evolution / 100)
            evolution = random.randint(0, 2) - 1
            self.jaugeFatigue = parent.body.jaugeFatigue + (parent.body.jaugeFatigue * evolution / 100)
            evolution = random.randint(0, 2) - 1
            self.jaugeReproduction = parent.body.jaugeReproduction + (parent.body.jaugeReproduction * evolution / 100)
            evolution = random.randint(0, 2) - 1
            self.esperance = parent.body.esperance + (parent.body.esperance * evolution * 3 / 100)

    def show(self):
        core.Draw.circle((255, 255, 255), self.position, self.size)
        super().show()

    def update(self):
        super().update()
