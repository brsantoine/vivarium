from agent import Agent
from herbivore_body import HerbivoreBody


class Herbivore(Agent):
    def __init__(self, parent):
        Agent.__init__(self, HerbivoreBody(parent))

    def createNew(self):
        return Herbivore(self)

    def filtrerPerception(self):
        manger = []
        fuir = []
        protect = []

        for otherAgent in self.perceptionList:
            if otherAgent.__class__.__name__ == "Vegetal":  # 70%
                if self.body.fatigue > 70*self.body.jaugeFaim/100:
                    otherAgent.dist = self.body.position.distance_to(otherAgent.position)
                    manger.append(otherAgent)
            else:
                otherAgent.dist = self.body.position.distance_to(otherAgent.body.position)
                if otherAgent.__class__.__name__ == "Carnivore":
                    fuir.append(otherAgent)
                if otherAgent.__class__.__name__ == "Superpredateur":
                    protect.append(otherAgent)

        manger.sort(key=lambda x: x.dist, reverse=False)
        fuir.sort(key=lambda x: x.dist, reverse=False)
        protect.sort(key=lambda x: x.dist, reverse=False)

        return manger, fuir, protect