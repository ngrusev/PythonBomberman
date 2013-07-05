DEFAULT_WIDTH = 50
DEFAULT_HEIGHT = 50
FADE_THRESHOLD = 50
FADE_SPEED = 3

class LevelElement:
    def __init__(self, x, y, width = DEFAULT_WIDTH, height = DEFAULT_HEIGHT):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.alive = True

    def get_sprite(self):
        raise NotImplementedError()

    def get_position(self):
        return (self.x, self.y)

    def is_solid(self):
        raise NotImplementedError()

    def update(self):
        pass

    def interact(self, element):
        pass

    def destroy(self):
        pass
