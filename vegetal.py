from item import Item

import core


class Vegetal(Item):
    def __init__(self):
        Item.__init__(self)

    def show(self):
        core.Draw.circle((255, 225, 0), self.position, self.size)
