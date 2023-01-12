import random
import time

from pygame import Vector2

import core
from fustrum import Fustrum


class Body:
    def __init__(self):
        self.position = Vector2(random.randint(0, core.WINDOW_SIZE[0]), random.randint(0, core.WINDOW_SIZE[1]))
        self.fustrum = Fustrum(150, self)
        self.dateNaissance = time.time()
        self.size = 5
        self.vitesse = Vector2()
        self.vitesseMax = 2
        self.acceleration = Vector2()
        self.accelerationMax = 10
        self.jaugeFaim = 0
        self.faim = 0
        self.jaugeFatigue = 0
        self.fatigue = 0
        self.jaugeReproduction = 0
        self.reproduction = 0
        self.esperance = 600
        self.isDead = False
        self.isSleeping = False
        self.timeSleeping = 0

    def show(self):
        core.Draw.circle((100, 100, 100), self.position, self.fustrum.radius, 1)

        if self.isSleeping:
            core.Draw.circle((255, 255, 255), self.position, self.size/2)

        if self.isDead:
            core.Draw.circle((0, 0, 0), self.position, self.size/2)


    def update(self):
        self.faim += 1
        self.fatigue += 1
        self.reproduction += 1

        if self.isSleeping:
            self.timeSleeping += 1

            if self.timeSleeping / core.fps >= 3:  # dors 3 secondes
                self.isSleeping = False
                self.timeSleeping = 0
                self.fatigue = 0

        if self.dateNaissance + self.esperance < time.time():
            self.isDead = True

        if self.fatigue >= self.jaugeFatigue:
            self.isSleeping = True

        if self.faim >= self.jaugeFaim:
            self.isDead = True

        if not self.isDead and not self.isSleeping:
            if self.acceleration.length() > self.accelerationMax:
                self.acceleration.scale_to_length(self.accelerationMax/self.size)
            self.vitesse += self.acceleration
            if self.vitesse.length() > self.vitesseMax:
                self.vitesse.scale_to_length(self.vitesseMax)
            self.position += self.vitesse

            core.Draw.line((255, 255, 255), self.position, self.position + self.acceleration * 100, 1)

        self.acceleration = Vector2()

        self.edge()

    def edge(self):
        if self.position.x <= self.size:
            self.vitesse.x *= -1
            self.position.x = 0 + self.size * 2
        if self.position.x + self.size >= core.WINDOW_SIZE[0]:
            self.vitesse.x *= -1
            self.position.x = core.WINDOW_SIZE[0] - self.size * 2
        if self.position.y <= self.size:
            self.vitesse.y *= -1
            self.position.y = 0 + self.size * 2
        if self.position.y + self.size >= core.WINDOW_SIZE[1]:
            self.vitesse.y *= -1
            self.position.y = core.WINDOW_SIZE[1] - self.size * 2
