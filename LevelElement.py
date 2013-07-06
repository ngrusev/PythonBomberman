DEFAULT_WIDTH = 50
DEFAULT_HEIGHT = 50
FADE_THRESHOLD = 50
FADE_SPEED = 3

class LevelElement:
    def __init__(self, x, y, width = DEFAULT_WIDTH, height = DEFAULT_HEIGHT):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._alive = True

    def getSprite(self):
        raise NotImplementedError()

    def getPosition(self):
        return (self._x, self._y)

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def getWidth(self):
        return self._width

    def getHeight(self):
        return self._height

    def isSolid(self):
        raise NotImplementedError()

    def update(self):
        pass

    def interact(self, element):
        pass

    def destroy(self):
        pass

    def isAlive(self):
        return self._alive
