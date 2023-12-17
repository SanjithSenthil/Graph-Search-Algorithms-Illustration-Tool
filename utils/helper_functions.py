# Retrieve the position clicked by the user on the window
def get_clicked_position(window_height, window_width, rows, columns, position):
    node_height = window_height // rows
    node_width = window_width // columns
    x, y = position
    row = y // node_height
    col = x // node_width
    return row, col

# Construct the shortest path between the start and end node
def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.set_path()
        draw()

# Manhattan distance
def h_score(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return abs(x2 - x1) + abs(y2 - y1)