import pygame
from queue import PriorityQueue
from utils.helper_functions import reconstruct_path

def dijkstra(draw, grid, start, end):
    visited = {node: False for row in grid for node in row}
    distance = {node: float("inf") for row in grid for node in row}
    distance[start] = 0
    came_from = {}
    priority_queue = PriorityQueue()
    priority_queue.put((0, start))

    while not priority_queue.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = priority_queue.get()[1]

        if visited[current]:
            continue

        visited[current] = True

        if current == end:
            reconstruct_path(came_from, end, draw)
            return True

        for neighbor in current.neighbors:
            weight = 1
            if distance[current] + weight < distance[neighbor]:
                came_from[neighbor] = current
                distance[neighbor] = distance[current] + weight
                priority_queue.put((distance[neighbor], neighbor))
            if neighbor != end and neighbor != start and not visited[neighbor]:
                neighbor.set_visiting()

        draw()

        if current != start:
            current.set_visited()

    return False