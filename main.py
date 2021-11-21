from pyamaze import maze, agent
from queue import PriorityQueue

def heuristic(x: list, y: list):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])

def a_star(m: maze):
    start = (m.rows, m.cols)
    cost_so_far = {cell: float('inf') for cell in m.grid}
    cost_so_far[start] = 0
    came_from = {cell: float('inf') for cell in m.grid}
    came_from[start] = heuristic(start, (1,1))

    frontier = PriorityQueue()
    frontier.put((came_from[start], came_from[start], start))

    path = {}

    while not frontier.empty():
        current = frontier.get()[2]
        if current == (1,1):
            break
        for d in 'ESNW':
            if m.maze_map[current][d] == True:
                if d == 'E':
                    cell = (current[0], current[1] + 1)
                elif d == 'S':
                    cell = (current[0] + 1, current[1])
                elif d == 'W':
                    cell = (current[0], current[1] - 1)
                elif d == 'N':
                    cell = (current[0] - 1, current[1])

                temp_costsofar= cost_so_far[current] + 1
                temp_camefrom = temp_costsofar + heuristic(cell, (1,1))

                if temp_costsofar < cost_so_far[cell]:
                    cost_so_far[cell] = temp_costsofar
                    came_from[cell] = temp_camefrom
                    frontier.put((temp_camefrom, heuristic(cell, (1,1)), cell))
                    path[cell] = current
    fordward_path = {}
    cell = (1,1)
    while cell != start:
        fordward_path[path[cell]] = cell
        cell = path[cell]
    return fordward_path


if __name__ == '__main__':
    m = maze()
    m.CreateMaze()
    path = a_star(m)

    a = agent(m)
    m.tracePath({a: path})
    m.run()