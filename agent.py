import random

from pygame import Vector2


class Agent:
    def __init__(self, body):
        self.uuid = random.randint(100000, 999999999)
        self.body = body
        self.perceptionList = []

    def createNew(self):
        pass

    def show(self):
        self.body.show()

    def update(self):
        move = Vector2(random.randint(-1, 1), random.randint(-1, 1))
        while move.length() == 0:
            move = Vector2(random.randint(-1, 1), random.randint(-1, 1))
        move.scale_to_length(move.length() * .1)
        self.body.acceleration += move

        manger, fuir, protect = self.filtrerPerception()

        if len(fuir) > 0:
            move = self.body.position - fuir[0].body.position
            move.scale_to_length(move.length() * .5)
            self.body.acceleration += move
        elif len(manger) > 0:
            if manger[0].__class__.__name__ == "Vegetal":
                move = manger[0].position - self.body.position
            else:
                move = manger[0].body.position - self.body.position
            move.scale_to_length(move.length() * .2)
            self.body.acceleration += move
        elif len(protect) > 0:
            move = protect[0].body.position - self.body.position
            move.scale_to_length(move.length() * .1)
            self.body.acceleration += move

    def filtrerPerception(self):
        return [], [], []
