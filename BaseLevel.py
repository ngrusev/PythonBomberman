class BaseLevel:
    def __init__(self, width, height, player):
        self.player = player
        player.current_level = self
        self.height = height
        self.width = width

    def is_element_position_valid(self, element, x, y):
        return (self.is_position_valid(x, y) and
            self.is_position_valid(x + element.width, y) and
            self.is_position_valid(x, y  + element.height) and
            self.is_position_valid(x + element.width, y + element.height))

    def is_position_valid(self, x, y):
        return (x >= 0 and x < self.width and
                y >= 0 and y < self.height)
    
