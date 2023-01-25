import random

from pygame import Vector2

import core
from agent import Agent
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

    for i in range(0, 25):
        core.memory('item').append(Vegetal())

    print("Setup END-----------")


def updateEnvironment():
    for agent in core.memory('agents'):
        for otherAgent in core.memory('agents'):
            if agent.body.position.distance_to(otherAgent.body.position) <= agent.body.size:
                if isinstance(agent, Carnivore) and isinstance(otherAgent, Herbivore):
                    agent.body.faim -= 15
                    core.memory('agents').remove(otherAgent)
                elif isinstance(agent, Superpredateur) and isinstance(otherAgent, Carnivore):
                    agent.body.faim -= 20
                    core.memory('agents').remove(otherAgent)
                elif isinstance(agent, Decomposeur) and isinstance(otherAgent, Agent) and otherAgent.body.isDead:
                    agent.body.faim -= 30
                    core.memory('agents').remove(otherAgent)

# todo add decomposeur in if in boucle for item
        if isinstance(agent, Herbivore):
            for item in core.memory('item'):
                if isinstance(item, Vegetal) and agent.body.position.distance_to(item.position) <= agent.body.size:
                    agent.body.faim -= 10
                    item.position = Vector2(random.randint(0, core.WINDOW_SIZE[0]), random.randint(0, core.WINDOW_SIZE[1]))

        if agent.body.reproduction >= agent.body.jaugeReproduction:
            agent.body.reproduction = 0
            core.memory('agents').append(agent.createNew())

    for item in core.memory('item'):
        if isinstance(item, Vegetal):
            for agent in core.memory('agents'):
                if isinstance(agent, Decomposeur) and item.position.distance_to(agent.body.position) <= item.size:
                    core.memory('agents').remove(agent)



def computePerception(agent):
    agent.perceptionList = []
    for otherAgent in core.memory('agents'):
        if agent.uuid != otherAgent.uuid:
            if agent.body.fustrum.inside(otherAgent.body):
                agent.perceptionList.append(otherAgent)
    for item in core.memory('item'):
        if isinstance(agent, Herbivore):
            if agent.body.fustrum.inside(item):
                agent.perceptionList.append(item)


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

    updateEnvironment()

core.main(setup, run)
