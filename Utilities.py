def intersecting(first, second):
    return (__is_point_in_element(first, second.x, second.y) or
            __is_point_in_element(first, second.x + second.width - 1, second.y) or
            __is_point_in_element(first, second.x, second.y + second.height - 1) or
            __is_point_in_element(first, second.x + second.width - 1, second.y + second.height - 1))
    
def __is_point_in_element(element, x, y):
    return (element.x <= x and x < element.x + element.width and
            element.y <= y and y < element.y + element.height)
