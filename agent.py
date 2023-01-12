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
        move.scale_to_length(move.length() * .05)
        self.body.acceleration += move

        manger, fuir, protect = self.filtrerPerception()

        for agentAManger in manger:
            move = agentAManger.body.position - self.body.position
            move.scale_to_length(move.length() * .1)
            self.body.acceleration += move

        for agentAFuir in fuir:
            move = self.body.position - agentAFuir.body.position
            move.scale_to_length(move.length() * .2)
            self.body.acceleration += move

        for agentPourProteger in protect:
            move = agentPourProteger.body.position - self.body.position
            move.scale_to_length(move.length() * .1)
            self.body.acceleration += move

    def filtrerPerception(self):
        return [], [], []
