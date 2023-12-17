import tkinter as tk

root = tk.Tk()
root.title("Instruction & Algorithm Explanation")
text1 = tk.Text(root, height=45, width=67, bg="lightyellow")

root.config(bg="lightyellow")
text1.config(state="normal", font=("Calibri", 14))
text1.config(highlightthickness=0)
text1.tag_configure("bold", font=("Calibri", 14, "bold"))

# Instruction
text1.insert(tk.INSERT," Instructions: ", "bold")
text1.insert(tk.INSERT,"\n 1.  To set the start node, click once anywhere on the grid where you want it to be located.\n       \n 2.  To set the end node, click once anywhere on the grid where you want it to be located\n       after placing the start node.\n       \n 3.  To add walls, click anywhere on the grid to place them in your desired location. You can\n       add multiple walls as needed.\n       \n 4.  Choose an algorithm and click the corresponding button to visualize the pathfinding\n       process.\n       \n 5.  If you want to start over, simply click the reset button and repeat the steps as above.\n\n",)

# Algorithm Explanation
text1.insert(tk.INSERT," The 5 Different Graph Search Algorithms: ", "bold")
text1.insert(tk.INSERT, "\n\n")

text1.insert(tk.INSERT," 1) Breadth First Search: ", "bold")
text1.insert(tk.INSERT,"Visits all nodes at the current depth level before moving on to\n      nodes at the next depth level. Guarantees the shortest path from the starting node to\n      the ending node.\n      Time Complexity: O(V + E)\n      Space Complexity: O(V)\n\n")

text1.insert(tk.INSERT," 2) Depth First Search: ", "bold")
text1.insert(tk.INSERT,"Visits nodes as far as possible along each branch before\n      backtracking. Does not always guarantee the shortest path from the starting node to\n      the ending node.\n      Time Complexity: O(V + E)\n      Space Complexity: O(V)\n\n")

text1.insert(tk.INSERT," 3) Dijkstra Algorithm: ", "bold")
text1.insert(tk.INSERT,"It is similar to a breadth first search but instead can be applied on\n      weighted graphs by using a priority queue to ensure that the shortest distance to each\n      node is always being examined first. Guarantees the shortest path from the starting\n      node to the ending node.\n      Time Complexity: O(V ^ 2)\n      Space Complexity: O(V)\n\n")

text1.insert(tk.INSERT," 4) A Star Search: ", "bold")
text1.insert(tk.INSERT,"It is an informed search algorithm that uses both the cost to reach the\n      current node and an estimate of the cost to reach the end node to determine the next\n      node to explore. Guarantees the shortest path from the starting node to the ending\n      node. The time and space complexity depends on the heuristic function and the\n      implementation of the algorithm.\n\n")

text1.insert(tk.INSERT," 5) Greedy Best First Search: ", "bold")
text1.insert(tk.INSERT,"It is an informed search algorithm that uses only an estimate\n      of the cost to reach the end node to determine the next node to explore. Does not \n      guarantee the shortest path from the start node to the end node. The time and space \n      complexity depends on the heuristic function and the implementation of the algorithm.")

text1.tag_add("bold", "3.0", "3.22")

text1.config(state="disabled")

text1.pack(padx=12,pady=11)

root.mainloop()