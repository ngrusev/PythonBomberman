import LevelElement

class BaseWall(LevelElement.LevelElement):
    def __init__(self, x, y):
        super().__init__(x, y)

    def isSolid(self):
        return True
