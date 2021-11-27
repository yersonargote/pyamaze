from pyamaze import maze
from node import PriorityQueue, Node


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
    frontier.push(Node(start, None, 0.0, heuristic(start, goal)))

    explored = {row: float('inf') for row in m.grid}
    explored[start] = 0

    path = {}
    search_path = [start]

    while not frontier.empty:
        current = frontier.pop().state
        search_path.append(current)
        if current == goal:
            break

        # Get the neighbors of the current node.
        for neighbor in m.getNeighbors(current[0], current[1]):
            new_cost = explored[current] + 1
            if new_cost < explored[neighbor]:
                explored[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, goal)
                frontier.push(Node(neighbor, current, new_cost, priority))
                path[neighbor] = current

    forward_path = {}
    cell = goal
    while cell != start:
        forward_path[path[cell]] = cell
        cell = path[cell]
    return search_path, path, forward_path