from queue import PriorityQueue
from pyamaze import maze


def heuristic(x: list, y: list):
    # Manhattan distance
    return abs(x[0] - y[0]) + abs(x[1] - y[1])


def a_star(m: maze, start: list, goal: list):
    """
    A* algorithm for finding a path from start to goal in a maze using the Manhattan distance heuristic function.
    """
    # Check if start and goal is None.
    if start == None or goal == None:
        return None, None, None
 
    # Check if start and goal are in the maze.
    if not m.isInMaze(start[0], start[1]) or not m.isInMaze(goal[0], goal[1]):
        return None, None, None
   
    # Create a priority queue for the open list.
    frontier = PriorityQueue()
    # Initialize the frontier with the start node and its cost.
    frontier.put((heuristic(start, goal), heuristic(start, goal) , start))

    explored = {row: float('inf') for row in m.grid}
    explored[start] = 0

    path = {}
    search_path = [start]

    while not frontier.empty():
        current = frontier.get()[2]
        search_path.append(current)
        if current == goal:
            break

        # Get the neighbors of the current node.
        for neighbor in m.getNeighbors(current[0], current[1]):
            new_cost = explored[current] + 1
            if new_cost < explored[neighbor]:
                explored[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, goal)
                frontier.put((priority, new_cost, neighbor))
                path[neighbor] = current

    forward_path = {}
    cell = m._goal
    while cell != start:
        forward_path[path[cell]] = cell
        cell = path[cell]
    return search_path, path, forward_path