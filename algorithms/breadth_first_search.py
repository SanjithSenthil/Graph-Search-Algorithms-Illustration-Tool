import pygame
from utils.helper_functions import reconstruct_path

def breadth_first_search(draw, start, end):
    visited = [start]
    queue = [start]
    path = {}

    while queue:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = queue.pop(0)

        if current == end:
            reconstruct_path(path, end, draw)
            return True

        for neighbor in current.neighbors:
            if neighbor not in visited:
                path[neighbor] = current
                visited.append(neighbor)
                queue.append(neighbor)
                neighbor.set_visiting()

        draw()

        if current != start:
            current.set_visited()

    return False