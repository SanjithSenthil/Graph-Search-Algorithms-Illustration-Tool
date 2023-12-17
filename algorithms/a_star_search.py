import pygame
from queue import PriorityQueue
from utils.helper_functions import reconstruct_path, h_score

def a_star_search(draw, grid, start, end):
    count = 0
    visited = PriorityQueue()
    visited.put((0, count, start))
    path = {}
    g = {node: float("inf") for row in grid for node in row}
    g[start] = 0
    f = {node: float("inf") for row in grid for node in row}
    f[start] = h_score(start.get_position(), end.get_position())
    visited_hash = {start}

    while not visited.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = visited.get()[2]
        visited_hash.remove(current)

        if current == end:
            reconstruct_path(path, end, draw)
            return True

        for neighbor in current.neighbors:
            temp_g = g[current] + 1
            if temp_g < g[neighbor]:
                path[neighbor] = current
                g[neighbor] = temp_g
                f[neighbor] = temp_g + h_score(neighbor.get_position(), end.get_position())
                if neighbor not in visited_hash:
                    count += 1
                    visited.put((f[neighbor], count, neighbor))
                    visited_hash.add(neighbor)
                    neighbor.set_visiting()

        draw()

        if current != start:
            current.set_visited()

    return False