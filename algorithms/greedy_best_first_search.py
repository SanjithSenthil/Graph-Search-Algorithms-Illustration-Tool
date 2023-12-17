import pygame
from queue import PriorityQueue
from utils.helper_functions import reconstruct_path, h_score

def greedy_best_first_search(draw, grid, start, end):
    count = 0
    priority_queue = PriorityQueue()
    priority_queue.put((0, count, start))
    came_from = {}
    f_score = {spot: float("inf") for row in grid for spot in row}
    f_score[start] = h_score(start.get_position(), end.get_position())
    priority_queue_hash = {start}

    while not priority_queue.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = priority_queue.get()[2]
        priority_queue_hash.remove(current)

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.set_end()
            start.set_start()
            return True

        for neighbor in current.neighbors:
            temp_f_score = h_score(neighbor.get_position(), end.get_position())
            if temp_f_score < f_score[neighbor]:
                came_from[neighbor] = current
                f_score[neighbor] = temp_f_score
                if neighbor not in priority_queue_hash:
                    count += 1
                    priority_queue.put((f_score[neighbor], count, neighbor))
                    priority_queue_hash.add(neighbor)
                    neighbor.set_visiting()

        draw()

        if current != start:
            current.set_visited()

    return False