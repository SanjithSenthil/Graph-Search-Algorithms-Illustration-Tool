import pygame
import time
from ui_components.grid import create_grid, draw_grid
from ui_components.button import Button
from algorithms.breadth_first_search import breadth_first_search
from algorithms.depth_first_search import depth_first_search
from algorithms.dijkstra import dijkstra
from algorithms.a_star_search import a_star_search
from algorithms.greedy_best_first_search import greedy_best_first_search
from utils.helper_functions import get_clicked_position
from pygame import mixer

pygame.init()
mixer.init()

mixer.music.load("assets/background_music.mp3")
# Set the preferred volume
mixer.music.set_volume(0.30)
# Set the number of times to repeat the music (-1 for infinite loop)
mixer.music.play(loops=-1)

# Create a window
window_height = 700
window_width = 800
height_offset = 103
window = pygame.display.set_mode((window_width, window_height+height_offset))
pygame.display.set_caption("Algorithm Animation")

# Create button objects
button_bfs = Button(0, 750, 130, 45, "BFS", (255, 255, 255), (0, 0, 0))
button_dfs = Button(140, 750, 130, 45, "DFS", (255, 255, 255), (0, 0, 0))
button_dijkstra = Button(280, 750, 130, 45, "DIJKSTRA", (255, 255, 255), (0, 0, 0))
button_astar = Button(420, 750, 130, 45, "A STAR", (255, 255, 255), (0, 0, 0))
button_greedy = Button(560, 750, 130, 45, "GREEDY", (255, 255, 255), (0, 0, 0))
button_reset = Button(702, 753, 95, 40,  "RESET", (255, 255, 255), (200, 0, 0))

# RGB Color Codes for control panel
panel_color = (245, 235, 235)

# Create text for statistics
font1 = pygame.font.SysFont("CalibriBold", 28)
font2 = pygame.font.SysFont("Calibri", 19)
text_color = (0, 0, 0)
first_stat = "Number of Visited Nodes: "
rendered_stat1 = font1.render(first_stat, True, text_color, (245, 235, 235))
x1_pos = 108
y1_pos = 712
second_stat = "Elapsed Time (ms): "
rendered_stat2 = font1.render(second_stat, True, text_color, (245, 235, 235))
x2_pos = 448
y2_pos = 712

def main(window, window_width):
    window.fill(panel_color)
    rows = 50
    columns = 50
    grid = create_grid(window_height, window_width, rows, columns)

    # Indicate if the start node is placed and points to the start node
    start = None
    # Indicate if the end node is placed and points to the end node
    end = None

    # Indicate if the window is running
    run = True
    # Indicate if the visualization tool has started
    started = None

    elapsed_time = 0
    number_of_visited_nodes = 0

    while run:

        # Draw the Graphical User Interface
        draw_grid(window, window_height, window_width, grid, rows, columns)
        button_bfs.draw(window)
        button_dfs.draw(window)
        button_dijkstra.draw(window)
        button_astar.draw(window)
        button_greedy.draw(window)
        button_reset.draw(window)
        window.blit(rendered_stat1, (x1_pos, y1_pos))
        window.blit(rendered_stat2, (x2_pos, y2_pos))

        # Display the number of visited nodes
        if number_of_visited_nodes == 0:
            first_value = ""
        else:
            first_value = str(number_of_visited_nodes)
        rendered_value3 = font2.render(first_value, True, text_color, (245, 235, 235))
        x3_pos = x1_pos + rendered_stat1.get_width()
        y3_pos = y1_pos-2
        window.blit(rendered_value3, (x3_pos, y3_pos))

        # Display the elapsed time
        if elapsed_time == 0:
            fourth_text = ""
        else:
            fourth_text = str(elapsed_time)
        rendered_text4 = font2.render(fourth_text, True, text_color, (245, 235, 235))
        x4_pos = x2_pos + rendered_stat2.get_width()
        y4_pos = y2_pos-2
        window.blit(rendered_text4, (x4_pos, y4_pos))

        for event in pygame.event.get():
            # User clicks the quit button on the window
            if event.type == pygame.QUIT:
                run = False

            # User clicks left mouse
            if pygame.mouse.get_pressed()[0] and not started:
                position = pygame.mouse.get_pos()    # Returns the x and y position of the mouse button clicked
                row, col = get_clicked_position(window_height, window_width, rows, columns, position)
                # User clicks on grid
                if row <= (rows - 1):
                    node = grid[row][col]
                    # Create a start node
                    if not start and node != end:
                        start = node
                        start.set_start()

                    # Create an end node
                    elif not end and node != start:
                        end = node
                        end.set_end()

                    # Create barrier nodes
                    elif node != end and node != start:
                        node.set_barrier()

            # User clicks right mouse
            elif pygame.mouse.get_pressed()[2] and not started:
                position = pygame.mouse.get_pos()  # Returns the x and y position of the mouse click
                row, col = get_clicked_position(window_height, window_width, rows, columns, position)
                # User clicks on grid
                if row <= (rows - 1):
                    node = grid[row][col]
                    node.reset()
                    if node == start:
                        start = None
                    elif node == end:
                        end = None

            # User clicks right mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                # User clicks Breadth first search button
                if button_bfs.check() == True and start and end and not started:
                    started = True
                    start_time = time.time()
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)

                    found = breadth_first_search(
                        lambda: draw_grid(window, window_height, window_width, grid, rows, columns), start, end)
                    end_time = time.time()
                    elapsed_time = round((end_time - start_time) * 1000, 2)
                    start.set_start()
                    end.set_end()
                    for row in grid:
                        for node in row:
                            if node.is_visited() or node.is_visiting() or node.is_path():
                                number_of_visited_nodes += 1
                    if not found:
                        pass

                # User clicks Depth first search button
                elif button_dfs.check() == True and start and end and not started:
                    started = True
                    start_time = time.time()
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)

                    found = depth_first_search(
                        lambda: draw_grid(window, window_height, window_width, grid, rows, columns), start, end)
                    end_time = time.time()
                    elapsed_time = round((end_time - start_time) * 1000, 2)
                    start.set_start()
                    end.set_end()
                    for row in grid:
                        for node in row:
                            if node.is_visited() or node.is_visiting() or node.is_path():
                                number_of_visited_nodes += 1
                    if not found:
                        pass

                # User clicks Dijkstra button
                elif button_dijkstra.check() == True and start and end and not started:
                    started = True
                    start_time = time.time()
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)

                    found = dijkstra(lambda: draw_grid(window, window_height, window_width, grid, rows, columns),
                                     grid, start, end)
                    end_time = time.time()
                    elapsed_time = round((end_time - start_time) * 1000, 2)
                    start.set_start()
                    end.set_end()
                    for row in grid:
                        for node in row:
                            if node.is_visited() or node.is_visiting() or node.is_path():
                                number_of_visited_nodes += 1
                    if not found:
                        pass

                # User clicks A star button
                elif button_astar.check() == True and start and end and not started:
                    started = True
                    start_time = time.time()
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)

                    found = a_star_search(lambda: draw_grid(window, window_height, window_width, grid, rows, columns), grid, start, end)
                    end_time = time.time()
                    elapsed_time = round((end_time - start_time) * 1000, 2)
                    start.set_start()
                    end.set_end()
                    for row in grid:
                        for node in row:
                            if node.is_visited() or node.is_visiting() or node.is_path():
                                number_of_visited_nodes += 1
                    if not found:
                        pass

                # User clicks Greedy button
                elif button_greedy.check() == True and start and end and not started:
                    started = True
                    start_time = time.time()
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)

                    found = greedy_best_first_search(lambda: draw_grid(window, window_height, window_width, grid, rows, columns), grid, start, end)
                    end_time = time.time()
                    elapsed_time = round((end_time - start_time) * 1000, 2)
                    start.set_start()
                    end.set_end()
                    for row in grid:
                        for node in row:
                            if node.is_visited() or node.is_visiting() or node.is_path():
                                number_of_visited_nodes += 1
                    if not found:
                        pass

                # User clicks Reset button
                if button_reset.check() == True:
                    start = None
                    end = None
                    started = None
                    grid = create_grid(window_height, window_width, rows, columns)
                    elapsed_time = 0
                    number_of_visited_nodes = 0
                    # Clear the area of the old value by filling with the background color
                    window.fill(panel_color, (x4_pos, y4_pos, rendered_text4.get_width(), rendered_text4.get_height()))
                    window.fill(panel_color, (x3_pos, y3_pos, rendered_value3.get_width(), rendered_value3.get_height()))

        pygame.display.update()

    # Close the window
    pygame.quit()

main(window, window_width)