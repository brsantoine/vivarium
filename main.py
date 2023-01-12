import random
from pygame.math import Vector2
import core
from carnivore import Carnivore
from decomposeur import Decomposeur
from herbivore import Herbivore
from superpredateur import Superpredateur
from vegetal import Vegetal


def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [1000, 700]

    core.memory("agents", [])
    core.memory("item", [])

    core.memory('agents').append(Carnivore(None))
    core.memory('agents').append(Herbivore(None))
    core.memory('agents').append(Superpredateur(None))
    core.memory('agents').append(Decomposeur(None))

    core.memory('item').append(Vegetal())

    print("Setup END-----------")


def updateEnvironment():
    for agent in core.memory('agents'):
        if agent.body.reproduction >= agent.body.jaugeReproduction:
            core.memory('agents').append(agent.__class__)


def computePerception(agent):
    agent.perceptionList = []
    for otherAgent in core.memory('agents'):
        if agent.uuid != otherAgent.uuid:
            if agent.body.fustrum.inside(otherAgent.body):
                agent.perceptionList.append(otherAgent)


def computeDecision(agent):
    agent.update()


def applyDecision(agent):
    agent.body.update()


def run():
    core.cleanScreen()

    # Display
    for agent in core.memory("agents"):
        agent.show()

    for item in core.memory("item"):
        item.show()

    for agent in core.memory("agents"):
        computePerception(agent)

    for agent in core.memory("agents"):
        computeDecision(agent)

    for agent in core.memory("agents"):
        applyDecision(agent)


core.main(setup, run)
