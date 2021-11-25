from pyamaze import maze, agent, COLOR, textLabel
from a_star import a_star

def main():
    # rows and columns of the maze
    rows, cols= (10, 10)

    # Point of the agent in the maze
    start = (10, 10)

    # Point of the goal in the maze
    goal = (1,1)

    # Create the maze with the given rows and columns
    m = maze(rows=rows, cols=cols)

    # Create maze with the given goal
    m.CreateMaze(x=goal[0], y=goal[1])

    # Solve the maze using A* algorithm
    search_path, path, fordward_path = a_star(m, start, goal)

    # Validate if a_star found a path
    if path == None or fordward_path == None or search_path == None:
        print("No path found")
        return

    # Create the agent that will be used to move the agent in the maze with the given path
    a = agent(m, footprints=True, color=COLOR.blue, filled=True)
    b = agent(m, goal[0], goal[1], footprints=True, color=COLOR.yellow, filled=True, goal=start)
    c = agent(m, start[0], start[1], footprints=True, color=COLOR.red, goal=goal)

    # Move the agent in the maze with the given path 
    m.tracePath({a: search_path}, delay=200)
    m.tracePath({b: path}, delay=200)
    m.tracePath({c: fordward_path}, delay=200)

    # Show the maze
    m.run()


if __name__ == '__main__':
    main()