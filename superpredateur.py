from agent import Agent
from superpredateur_body import SuperpredateurBody


class Superpredateur(Agent):
    def __init__(self, parent):
        Agent.__init__(self, SuperpredateurBody(parent))

    def createNew(self):
        return Superpredateur(self)

    def filtrerPerception(self):
        manger = []
        fuir = []
        protect = []

        for otherAgent in self.perceptionList:
            otherAgent.dist = self.body.position.distance_to(otherAgent.body.position)
            if otherAgent.__class__.__name__ == "Carnivore":
                manger.append(otherAgent)

        manger.sort(key=lambda x: x.dist, reverse=False)

        return manger, fuir, protect
