import SceneElement

WIDTH = 50
HEIGHT = 50

class BaseWall(SceneElement.SceneElement):
    def __init__(self, x, y):
        super().__init__(WIDTH, HEIGHT, x, y)

    def is_solid(self):
        return True
