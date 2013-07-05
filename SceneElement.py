class SceneElement:
    def __init__(self, width, height, x, y):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def get_sprite(self):
        raise NotImplementedError()

    def get_position(self):
        return (self.x, self.y)

    def is_solid(self):
        raise NotImplementedError()
