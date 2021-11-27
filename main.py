from pyamaze import maze, agent, COLOR, textLabel
from a_star import a_star
from bfs import BFS

def main():

    value: int = 8
    
    # rows and columns of the maze
    rows, cols= (value, value)

    # Point of the agent in the maze
    start = (value, value)

    # Point of the goal in the maze
    goal = (1,1)

    # Create the maze with the given rows and columns
    m = maze(rows=rows, cols=cols)

    # Create maze with the given goal
    m.CreateMaze(x=goal[0], y=goal[1])

    # Solve the maze using A* algorithm
    search_path, path, forward_path = a_star(m, start, goal)

    # Solve the maze using BFS algorithm
    bfs_search_path, bfs_path, bfs_forward_path = BFS(m, start)

    # Validate if a_star found a path
    if forward_path == None or path == None or search_path == None:
        print("No path found")
        return

    # Create the agent that will be used to move the agent in the maze with the given path
    a = agent(m, footprints=True, color=COLOR.blue, filled=True)
    b = agent(m, goal[0], goal[1], footprints=True, color=COLOR.yellow, filled=True, goal=start)
    c = agent(m, start[0], start[1], footprints=True, color=COLOR.red, goal=goal)

    # Create agent that will be used to move the agent in the maze with the given path
    # d = agent(m, footprints=True, color=COLOR.yellow)
    # e = agent(m, start[0], start[1], footprints=True, color=COLOR.green, goal=goal)


    # Move the agent in the maze with the given path 
    m.tracePath({a: search_path}, delay=200)
    m.tracePath({b: path}, delay=200)
    m.tracePath({c: forward_path}, delay=200)

    # Move the agent in the maze with the given path BFS
    # m.tracePath({d: bfs_search_path}, delay=200)
    # m.tracePath({e: forward_path}, delay=200)

    # Show the maze
    m.run()


if __name__ == '__main__':
    main()