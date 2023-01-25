from agent import Agent
from carnivore_body import CarnivoreBody


class Carnivore(Agent):
    def __init__(self, parent):
        Agent.__init__(self, CarnivoreBody(parent))

    def createNew(self):
        return Carnivore(self)

    def filtrerPerception(self):
        manger = []
        fuir = []
        protect = []

        for otherAgent in self.perceptionList:
            otherAgent.dist = self.body.position.distance_to(otherAgent.body.position)
            if otherAgent.__class__.__name__ == "Herbivore" and self.body.fatigue > 50*self.body.jaugeFaim/100:  # 50% de faim
                manger.append(otherAgent)
            if otherAgent.__class__.__name__ == "Superpredateur":
                fuir.append(otherAgent)

        manger.sort(key=lambda x: x.dist, reverse=False)
        fuir.sort(key=lambda x: x.dist, reverse=False)

        return manger, fuir, protect

