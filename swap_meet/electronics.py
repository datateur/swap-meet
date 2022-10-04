from .item import Item


class Electronics(Item):
    def __init__(self, category = "Electronics", condition = 0):
        Item.__init__(self, category, condition)
    
    def __str__(self):
        return "A gadget full of buttons and secrets."