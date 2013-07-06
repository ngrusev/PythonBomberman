def intersecting(first, second):
    return __hasPointIn(first, second) or __hasPointIn(second, first)

def __hasPointIn(first, second):
    return (__isPointInElement(first, second.getX(), second.getY()) or
            __isPointInElement(first, second.getX() + second.getWidth() - 1, second.getY()) or
            __isPointInElement(first, second.getX(), second.getY() + second.getHeight() - 1) or
            __isPointInElement(first, second.getX() + second.getWidth() - 1, second.getY() + second.getHeight() - 1))

def __isPointInElement(element, x, y):
    return (element.getX() <= x and x < element.getX() + element.getWidth() and
            element.getY() <= y and y < element.getY() + element.getHeight())

def modDecrease(value):
    if value > 0:
        value -= 1
    elif value < 0:
        value += 1
    return value
