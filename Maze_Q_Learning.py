import Maze
import numpy as np
import random

class Agent:
    def __init__(self, rand, alpha, gamma):
        self.rand = rand
        self.alpha = alpha
        self.gamma = gamma
        self.maze = Maze.Maze()
        self.Q_table = np.random.uniform(low=-1, high=1, size=(120, 4))

    def policy(self):
        direction = None
        if random.random() < self.rand:
            rand = random.random()
            if rand < 0.25:
                direction = Maze.Direction.UP
            elif rand < 0.5:
                direction = Maze.Direction.DOWN
            elif rand < 0.75:
                direction = Maze.Direction.LEFT
            else:
                direction = Maze.Direction.RIGHT
        else:
            if np.argmax(self.Q_table[self.maze.position]) == 0:
                direction = Maze.Direction.UP
            elif np.argmax(self.Q_table[self.maze.position]) == 1:
                direction = Maze.Direction.DOWN
            elif np.argmax(self.Q_table[self.maze.position]) == 2:
                direction = Maze.Direction.RIGHT
            elif np.argmax(self.Q_table[self.maze.position]) == 3:
                direction = Maze.Direction.LEFT
        return direction

    def proceed(self, direction):
        pre_state = self.maze.get_position()
        direction = self.policy()
        action = 0
        if direction == Maze.Direction.UP:
            action = 0
        elif direction == Maze.Direction.DOWN:
            action = 1
        elif direction == Maze.Direction.RIGHT:
            action = 2
        else:
            action = 3
        self.maze.step(direction)
        reward = self.maze.reward()
        next_state = self.maze.get_position()
        self.update_Q(pre_state, action, reward, next_state)

    def update_Q(self, pre_state, action, reward, next_state):
        self.Q_table[pre_state][action] = (1 - self.alpha) * self.Q_table[pre_state][action] + \
                                          self.alpha * (reward + self.gamma * np.max(self.Q_table[next_state]))

    def zero_random(self):
        self.rand = 0