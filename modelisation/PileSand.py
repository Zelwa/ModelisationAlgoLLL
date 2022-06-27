import time
from Grid import Grid
from Application import Application

class PileSand:

    def __init__(self,width,height,H, h):
        self.grid = Grid(width,height,h)
        self.H = H
        self.h = h
        self.application = Application(self.grid)


    def transition(self,i):
                    if(i==self.grid.height - 1) & (self.grid.pile_size(i)-self.grid.pile_size(i-1)>self.H):
                        self.grid.change_grid(self.h,i,"sub")
                        self.grid.change_grid(self.h,i-1,"add")
                    elif(i== 0) & (self.grid.pile_size(i)-self.grid.pile_size(i + 1)>self.H):
                        self.grid.change_grid(self.h,i + 1,"add")
                        self.grid.change_grid(self.h,i,"sub")
                    elif i > 0 and self.grid.pile_size(i) - self.grid.pile_size(i - 1) > self.H:
                        self.grid.change_grid(self.h, i - 1, "add")
                        self.grid.change_grid(self.h, i, "sub")
                    elif i > 0 and self.grid.pile_size(i) - self.grid.pile_size(i + 1) > self.H:
                        self.grid.change_grid(self.h, i + 1, "add")
                        self.grid.change_grid(self.h, i, "sub")


    def verification(self,i):
        if 0 < i < self.grid.height-1:
            if self.grid.pile_size(i) - self.grid.pile_size(i + 1) >self.H or self.grid.pile_size(i) - self.grid.pile_size(i - 1) > self.H :
                return True
        elif i == 0 and self.grid.pile_size(i) - self.grid.pile_size(i + 1) >self.H:
            return True
        elif i == self.grid.height-1 and self.grid.pile_size(i) - self.grid.pile_size(i - 1) >self.H:
                return True
        return False


    def is_over(self):
        for i in range(self.grid.get_height()-1):
            if self.grid.pile_size(i) - self.grid.pile_size(i + 1) >self.H:
                return False
            if self.grid.pile_size(i +1) - self.grid.pile_size(i) >self.H:
                return False
        if self.grid.pile_size(self.grid.get_height()-1) - self.grid.pile_size(self.grid.get_height()-2) >self.H :
            return False
        return True


    def string(self):
        print(self.h)
        print(self.H)
        print(self.grid.grid_to_string())



    def game_representation(self,duree_iteration):
        while not self.is_over():
            for i in range(self.grid.height):
                if self.verification(i):
                    size = self.grid.pile_size(i)
                    time.sleep(duree_iteration)
                    print("\n")
                    self.application.update_grid(i,size,self.h)
                    self.transition(i)
                    self.application.update()
                    for j in range(self.h):
                        self.application.d[ "label{0}{1}".format(self.grid.width - size + j, i) ].configure(bg='white')
        time.sleep(duree_iteration)
        print("\n")
        self.grid.grid_to_string()
        self.application.show_grid()
        self.application.mainloop()


