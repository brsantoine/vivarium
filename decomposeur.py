from agent import Agent
from decomposeur_body import DecomposeurBody
from vegetal import Vegetal


class Decomposeur(Agent):
    def __init__(self, parent):
        Agent.__init__(self, DecomposeurBody(parent))

    def createNew(self):
        return Decomposeur(self)

    def filtrerPerception(self):
        manger = []
        fuir = []
        protect = []

        for otherAgent in self.perceptionList:
            otherAgent.dist = self.body.position.distance_to(otherAgent.body.position)
            if (isinstance(otherAgent, Agent) and otherAgent.body.isDead and not isinstance(otherAgent, Decomposeur)) or otherAgent.__class__.__name__ == "Vegetal":
                manger.append(otherAgent)

        manger.sort(key=lambda x: x.dist, reverse=False)

        return manger, fuir, protect
