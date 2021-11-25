from queue import PriorityQueue
from pyamaze import maze
from utils import DIRECTIONS


def heuristic(x: list, y: list):
    # Manhattan distance
    return abs(x[0] - y[0]) + abs(x[1] - y[1])

def a_star(m: maze, start: list, goal: list):
    """
    A* algorithm for finding a path from start to goal in a maze using the Manhattan distance heuristic function.
    """

    # Evalue if start and goal are in the maze.
    if not m.isInMaze(start[0], start[1]) or not m.isInMaze(goal[0], goal[1]):
        return None, None, None
    
    # Evalue if start and goal is None.
    if start == None or goal == None:
        return None, None, None
    
    # Create a priority queue for the open list.
    frontier = PriorityQueue()
    # Initialize the frontier with the start node and its cost.
    frontier.put((heuristic(start, goal), heuristic(start, goal) , start))

    cost_so_far = {row: float('inf') for row in m.grid}
    cost_so_far[start] = 0
    came_from = {row: float('inf') for row in m.grid}
    came_from[start] = heuristic(start, goal)

    path = {}
    search_path = [start]

    while not frontier.empty():
        current = frontier.get()[2]
        search_path.append(current)
        if current == goal:
            break

        # Get the neighbors of the current node.
        for neighbor in m.getNeighbors(current[0], current[1]):
            new_cost = cost_so_far[current] + 1
            if new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, goal)
                frontier.put((priority, new_cost, neighbor))
                came_from[neighbor] = current
                path[neighbor] = current

    forward_path = {}
    cell = m._goal
    while cell != start:
        forward_path[path[cell]] = cell
        cell = path[cell]
    return search_path, path, forward_path