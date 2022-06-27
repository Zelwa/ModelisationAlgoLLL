import random

"""
'''                  [["[ ]","[ ]","[ ]","[ ]"],
                     ["[ ]","[]","[ ]","[ ]"],
                     ["[ ]","[X]","[X]","[ ]"],
                     ["[X]","[X]","[X]","[X]"],
                     ["[X]","[X]","[X]","[X]"]
                     
                     ]'''
"""
class Grid:
    def __init__(self, width, height ,h ):
        self.grid = []
        self.h = h
        self.width= width
        self.height=height
        for i in range(self.width):
            self.grid.append([])
            for j in range(height):
                self.grid[i].append("[ ]")
        for m in range(height):
            size = random.randint(1, self.width - h )
            for p in range(size):
                self.grid[self.width-p -1][m] = "[X]"


    def get_grid(self):
        return self.grid

    def grid_to_string(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                print(self.grid[i][j], end=" ")
            print("")

    def pile_size(self, index):
        size = 0
        for i in range(len(self.grid)):
            if self.grid[i][index] != "[ ]":
                size += 1
        return size

    def max_size(self):
        temp = 0
        for i in range (self.height):
            size = self.pile_size(i)
            if size > temp:
                temp = size
        return temp

    def change_grid(self, value, index, stat):
        try:
            for h in range(value):
                if(stat == "add"):
                    self.grid[self.width-(self.pile_size(index)+1)][index]= "[X]"
                if(stat == "sub"):
                    self.grid[self.width-(self.pile_size(index))][index]="[ ]"
        except:
            print("Sortie de grille")
            raise


    def get_height(self):
        return self.height

    def get_width(self):
        return self.width
