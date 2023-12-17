import pygame

class Node:
    def __init__(self, row, column, height, width, total_rows):
        self.row = row
        self.column = column
        self.x = width * column
        self.y = height * row
        self.height = height
        self.width = width
        self.color = normal_color
        self.neighbors = []
        self.total_rows = total_rows

    def get_position(self):
        return self.row, self.column

    def is_start(self):
        return self.color == start_color

    def is_end(self):
        return self.color == end_color

    def is_visiting(self):
        return self.color == visiting_color

    def is_visited(self):
        return self.color == visited_color

    def is_path(self):
        return self.color == path_color

    def is_barrier(self):
        return self.color == barrier_color

    def set_start(self):
        self.color = start_color

    def set_end(self):
        self.color = end_color

    def set_visiting(self):
        self.color = visiting_color

    def set_visited(self):
        self.color = visited_color

    def set_path(self):
        self.color = path_color

    def set_barrier(self):
        self.color = barrier_color

    def reset(self):
        self.color = normal_color

    def __lt__(self, other):
        return False

    def update_neighbors(self, grid):
        # Check if the above node is a neighbor
        if self.row > 0 and not grid[self.row - 1][self.column].is_barrier():
            self.neighbors.append(grid[self.row - 1][self.column])

        # Check if the below node is a neighbor
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.column].is_barrier():
            self.neighbors.append(grid[self.row + 1][self.column])

        # Check if the node left to it is a neighbor
        if self.column > 0 and not grid[self.row][self.column - 1].is_barrier():
            self.neighbors.append(grid[self.row][self.column - 1])

        # Check if the node right to it is a neighbor
        if self.column < self.total_rows - 1 and not grid[self.row][self.column + 1].is_barrier():
            self.neighbors.append(grid[self.row][self.column + 1])

    # Draw a node on the window
    def draw_node(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))


# RGB Color Codes for node
start_color = (30, 145, 255)
end_color = (0, 205, 210)
visiting_color = (200, 0, 0)
visited_color = (0, 200, 0)
path_color = (255, 215, 0)
barrier_color = (110, 110, 110)
normal_color = (50, 50, 50)