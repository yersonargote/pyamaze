from pyamaze import maze, agent, COLOR, textLabel
from queue import PriorityQueue

def heuristic(x: list, y: list):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])

def a_star(m: maze, start: list, goal: list):
    if start == None or goal == None:
        return None, None, None
    
    frontier = PriorityQueue()
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

                temp_costsofar = cost_so_far[current] + 1
                temp_camefrom = temp_costsofar + heuristic(cell, goal)

                if temp_costsofar < cost_so_far[cell]:
                    path[cell] = current
                    cost_so_far[cell] = temp_costsofar
                    came_from[cell] = temp_camefrom + heuristic(cell, goal)
                    frontier.put((came_from[cell], heuristic(cell, goal), cell))

    fordward_path = {}
    cell = m._goal
    while cell != start:
        fordward_path[path[cell]] = cell
        cell = path[cell]
    return search_path, path, fordward_path


if __name__ == '__main__':
    rows, cols= (10, 10)
    start = (10, 10)
    goal = (1,1)

    m = maze(rows=rows, cols=cols)
    m.CreateMaze(x=goal[0], y=goal[1])

    search_path, path, fordward_path = a_star(m, start, goal)

    if path == None or fordward_path == None or search_path == None:
        print("No path found")
    else:
        a = agent(m, footprints=True, color=COLOR.blue, filled=True)
        b = agent(m, goal[0], goal[1], footprints=True, color=COLOR.yellow, filled=True, goal=start)
        c = agent(m, start[0], start[1], footprints=True, color=COLOR.red, goal=goal)
        m.tracePath({a: search_path}, delay=200)
        m.tracePath({b: path}, delay=200)
        m.tracePath({c: fordward_path}, delay=200)
        m.run()