import tkinter as tk
from tkinter import *


class Application(tk.Tk):
    def __init__(self, grid):
        self.grid = grid
        self.d ={}
        tk.Tk.__init__(self)
        self.width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight()
        self.configure(background='black')
        self.create_grid()


    def create_grid(self):
        for i in range (self.grid.width ):
            for j in range (self.grid.height ):
                self.d["label{0}{1}".format(i,j)] = Label(self, bg ='white')
                self.d["label{0}{1}".format(i, j)].grid(row=i, column=j,ipadx =(self.width / self.grid.height)/4 , ipady = self.height / (self.grid.width * 4), padx = '1',pady='1')
                if self.grid.grid[i][j] == "[X]":
                    self.d["label{0}{1}".format(i, j)].configure(bg="red")


    def update_grid(self,column,size,h):
        for i in range(self.grid.width):
            for j in range(self.grid.height):
                if self.grid.grid[ i ][ j ] == "[X]":
                    self.d[ "label{0}{1}".format(i, j) ].configure(bg="red")
        for i in range(h):
            self.d[ "label{0}{1}".format(self.grid.width - size + i , column) ].configure(bg='yellow')



    def show_grid(self):
        for i in range(self.grid.width):
            for j in range(self.grid.height):
                if self.grid.grid[ i ][ j ] == "[X]":
                    self.d[ "label{0}{1}".format(i, j) ].configure(bg="red")








