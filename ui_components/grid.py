import pygame
from ui_components.node import Node

# Create a grid and store it through a data structure
def create_grid(window_height, window_width, rows, columns):
    grid = []
    node_height = window_height // rows
    node_width = window_width // columns
    for i in range(rows):
        grid.append([])
        for j in range(columns):
            node = Node(i, j, node_height, node_width, rows)
            grid[i].append(node)
    return grid

# Draw a line on the window
def draw_line(window, window_height, window_width, rows, columns):
    node_height = window_height // rows
    node_width = window_width // columns
    # Draw horizontal lines
    for i in range(rows):
        pygame.draw.line(window, line_color, (0, i * node_height), (window_width, i * node_height))
    # Draw vertical lines
    for i in range(columns):
        pygame.draw.line(window, line_color, (i * node_width, 0), (i * node_width, window_height-1))

# Draw the grid on the window
def draw_grid(window, window_height, window_width, grid, rows, columns):
    # Draw all nodes
    for row in grid:
        for node in row:
            node.draw_node(window)
    # Draw all lines
    draw_line(window, window_height, window_width, rows, columns)
    pygame.display.update()

# RGB Color Codes for grid
line_color = (0, 0, 0)