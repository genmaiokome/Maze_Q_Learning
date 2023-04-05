from Maze_Q_Learning import Agent
import os
import time
if __name__ == "__main__":
    agent = Agent(0.2, 0.1, 0.99)
    agent.maze.initialize()

    episode = 500
    limit = 1500

    for i in range(episode):
        agent.maze.initialize()
        for j in range(limit):
            os.system('clear')
            print("{}episode, {}step".format(i, j))
            agent.proceed(agent.policy())
            agent.maze.print_map()
            if agent.maze.is_goal():
                agent.maze.initialize()
                break
