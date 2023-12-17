import pygame
from utils.helper_functions import reconstruct_path

def depth_first_search(draw, start, end):
    visited = {start}
    stack = [start]
    path = {}

    while stack:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = stack.pop()

        if current == end:
            reconstruct_path(path, end, draw)
            return True

        if current not in visited:
            visited.add(current)
            if current != start:
                current.set_visiting()

        for neighbor in current.neighbors:
            if neighbor not in visited:
                stack.append(neighbor)
                path[neighbor] = current

        draw()

        if current != start:
            current.set_visited()

    return False