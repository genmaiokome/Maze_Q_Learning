import time
import random
import os

class Direction():
    UP = -12
    DOWN = + 12
    LEFT = -1
    RIGHT = +1


class Maze:
    def __init__(self):
        self.maze = [
            "□", "□", "□", "□", "□", "□", "□", "□", "□", "□", "□", "□",
            "□", "S", " ", " ", " ", " ", " ", " ", " ", " ", " ", "□",
            "□", "□", " ", "×", " ", "□", "□", "□", "□", "□", "□", "□",
            "□", "□", " ", "×", " ", "□", " ", " ", " ", "×", " ", "□",
            "□", "□", " ", "×", "□", "□", " ", "×", " ", " ", " ", "□",
            "□", "□", " ", "×", "□", "□", " ", "□", "□", "□", " ", "□",
            "□", "□", " ", " ", "□", "□", " ", "□", "□", "□", " ", "□",
            "□", " ", "×", " ", " ", "×", " ", " ", " ", "□", " ", "□",
            "□", " ", " ", " ", " ", " ", " ", " ", " ", "□", "G", "□",
            "□", "□", "□", "□", "□", "□", "□", "□", "□", "□", "□", "□"
        ]
        self.position = 13

    def initialize(self):
        self.position = 13

    def print_map(self):
        for y in range(len(self.maze)):
            if (y + 1) % 12 != 0:
                if y == self.position:
                    print("P", end='')
                else:
                    print(self.maze[y], end='')                    
            else:
                if y == self.position:
                    print("P")
                else:
                    print(self.maze[y])


    def step(self, direction):
        if direction + self.position>= 0 and \
            direction + self.position <= 120 and \
            self.maze[direction + self.position] != "□":
            self.position = self.position + direction

    
    def is_goal(self):
        if self.maze[self.position] == "G":
            return True
        else:
            return False
        
    def reward(self):
        if self.maze[self.position] == "×":
            return -1
        elif self.maze[self.position] == " " or self.maze[self.position] == "S":
            return -0.5
        else:
            return 0
        
    def get_position(self):
        return self.position
