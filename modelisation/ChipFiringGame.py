import time
from Grid import Grid
from Application import Application

class ChipFiringGame:

    def __init__(self,width,height,H, h):
        self.grid = Grid(width,height,h)
        self.H = H
        self.h = h
        self.application = Application(self.grid)

    def transition(self, index):
        pile_size = self.grid.pile_size(index)
        if index != 0 and index != self.grid.height - 1 and pile_size >= self.h:
            pile_sizea = self.grid.pile_size(index - 1)
            pile_sizeb = self.grid.pile_size(index + 1)
            for i in range(self.h):
                self.grid.grid[self.grid.width - pile_sizea - 1 - i][index - 1] = "[X]"
                self.grid.grid[self.grid.width - pile_sizeb - 1 - i][index + 1] = "[X]"
            for m in range(2*self.h):
                self.grid.grid[self.grid.width - pile_size + m][index] = "[ ]"
        if index == 0 and pile_size >= self.H:
            pile_sizeb = self.grid.pile_size(index + 1)
            for i in range(self.h):
                self.grid.grid[self.grid.width - pile_sizeb - 1 - i][index + 1] = "[X]"
            for m in range(2*self.h):
                self.grid.grid[self.grid.width - pile_size + m][index] = "[ ]"
        if index == self.grid.height - 1 and pile_size >= self.H:
            pile_sizea = self.grid.pile_size(index - 1)
            for i in range(self.h):
                self.grid.grid[ self.grid.width - pile_sizea - 1 - i ][ index - 1 ] = "[X]"
            for m in range(2 * self.h):
                self.grid.grid[ self.grid.width - pile_size + m ][ index ] = "[ ]"


    def is_over(self):
        for i in range(self.grid.height):
            if self.grid.pile_size(i) > self.H:
                return False
        return True


    def game_representation(self,duree_iteration):
        j = 0
        while not self.is_over():
            for i in range(self.grid.height):
                size = self.grid.pile_size(i)
                if size > self.H:
                    print("\n")
                    self.application.update_grid(i,size,2 * self.h)
                    self.grid.grid_to_string()
                    self.transition(i)
                    time.sleep(duree_iteration)
                    self.application.update()
                    for j in range(2 * self.h):
                        self.application.d[ "label{0}{1}".format(self.grid.width - size + j, i) ].configure(bg='white')
        time.sleep(duree_iteration)
        print("\n")
        self.grid.grid_to_string()
        self.application.show_grid()
        self.application.mainloop()





