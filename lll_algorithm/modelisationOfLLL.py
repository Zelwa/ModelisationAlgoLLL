import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class modelisationOfLLL(tk.Tk):
    def __init__(self, width, height, H):
        #Initialisation de la fenetre
        tk.Tk.__init__(self)
        self.attributes('-fullscreen', True)
        self.fullScreenState = False
        self.bind("<F11>", self.toggleFullScreen)
        self.bind("<Escape>", self.quitFullScreen)
        self.geometry(str(self.winfo_screenwidth())+'x'+str(self.winfo_screenheight()))
        self.minsize(480, 360)
        self.config(bg="white")
        self.title("Modélisation de l'algorithme LLL")
        #Frame du canvas et de la courbe
        self.frame = Frame(self,width=width, height=height, bg="white")
        self.frame.pack(expand=YES)
        #Fini
        #Button next
        self.button = Button(self.frame,text="Next",font=("Courrier",25),bg="gray",command=lambda: self.okVar.set(1))
        self.button.pack()
        #Taille unique au canvas
        self.width_canvas = width*2/3
        self.height_canvas = height*2/3
        self.width_p = 0
        #Liste de toutes les hauteurs et des canvas
        self.heights_list = None
        self.canvas = None
        self.canvas_matplot = None
        self.value_ratio = 0.0
        #Parametre liés aux CFG
        self.H = H

    #Touche bind
    def toggleFullScreen(self,event):
        self.fullScreenState = not self.fullScreenState
        self.attributes("-fullscreen", self.fullScreenState)
    def quitFullScreen(self,event):
        self.fullScreenState = False
        self.attributes("-fullscreen", self.fullScreenState)

    def ratio(self):
        max=0
        min=99999999
        for i in range(0,len(self.heights_list)):
            if max < abs(self.heights_list[i]):
                max = abs(self.heights_list[i])
            if min > abs(self.heights_list[i]):
                min = abs(self.heights_list[i])
        return (self.height_canvas/2)/max
    #Création d'une figure
    def new_plot(self):
        self.fig = matplotlib.pyplot.figure()
        self.plot = self.fig.add_subplot(111)
        self.plot.set_title("Avancée du LLL")
        self.plot.set_xlim(0, 1)
        self.plot.set_ylim(0, len(self.heights_list))
        self.plot.set_xlabel('Iteration')
        self.plot.set_ylabel('Index')
        self.plot.plot([])
        self.canvas_matplot = FigureCanvasTkAgg(self.fig,master=self.frame)
        self.canvas_matplot.get_tk_widget().pack()
    #Création d'un canvas comportant chaque pile
    def new_canvas(self, heights_list):
        self.canvas = Canvas(self.frame,width=self.width_canvas, height=self.height_canvas, bg='white')
        self.heights_list = heights_list
        print(self.heights_list)
        self.value_ratio = self.ratio()
        self.width_p = self.width_canvas / len(heights_list)
        for i in range(0, len(self.heights_list)):
            self.canvas.create_rectangle(self.width_p * i, self.height_canvas / 2,(self.width_p * i) + self.width_p,self.height_canvas / 2 - heights_list[i] * self.value_ratio / 2)
            if heights_list[i] < 0:
                self.canvas.itemconfig(i + 1, outline='#43a550',fill="#82d67e")
            else:
                self.canvas.itemconfig(i + 1, outline='#ed2525', fill="#f26565")
        #alpha
        self.canvas.create_rectangle(0, 0, 0, 0)
        self.canvas.create_line(0, self.height_canvas/2 - self.H*self.value_ratio/2, self.width_canvas, self.height_canvas/2 - self.H*self.value_ratio/2, fill="gray", width=self.height_canvas*0.005)
        self.canvas.pack()
    #Creation frame
    def creation_frame(self, heights_list):
        self.new_canvas(heights_list)
        self.new_plot()
        self.update()
    #Mise à jour du canvas
    def update_modelisation(self, new_heights_list, position,alpha,continu):
        self.heights_list = new_heights_list
        for i in range(0, len(self.heights_list)):
            self.canvas.coords(i+1, self.width_p * i, self.height_canvas/2, (self.width_p * i) + self.width_p, self.height_canvas/2 - self.heights_list[i]*self.value_ratio/2)
            if self.heights_list[i] < 0:
                self.canvas.itemconfig(i+1, outline='#43a550', fill="#82d67e")
            else:
                self.canvas.itemconfig(i+1, outline='#ed2525', fill="#f26565")
        if continu:
            if 0 <= position <= len(self.heights_list):
                self.canvas.coords(len(self.heights_list) + 1, self.width_p * position, self.height_canvas/2 - self.heights_list[position] * self.value_ratio/2, (self.width_p * position) + self.width_p,self.height_canvas/2 - self.heights_list[position] * self.value_ratio/2 + alpha* self.value_ratio/2)
                if self.heights_list[position] < 0:
                    self.canvas.itemconfig(len(self.heights_list) + 1, outline='#43a550', fill="#43a550")
                else:
                    self.canvas.itemconfig(len(self.heights_list) + 1, outline='#ed2525', fill="#ed2525")
            else:
                sys.exit("Position inaccessible ")
            self.okVar = tk.IntVar()
            self.wait_variable(self.okVar)
        else:
            self.canvas.coords(len(self.heights_list) + 1, 0, 0, 0, 0)
            self.button.destroy()
            fontStyle = tkFont.Font(family="Lucida Grande", size=20)
            text = Label(self.frame, text="C'est fini!", bg="#4db0dd", font=fontStyle, fg="white")
            text.pack(side=TOP)
    # Mise à jour du plot
    def update_plot(self, list_i, iterator):
        self.plot.clear()
        self.plot.set_title("Avancée du LLL")
        self.plot.set_xlim(0, iterator)
        self.plot.set_ylim(0, len(self.heights_list))
        self.plot.set_xlabel('Iteration')
        self.plot.set_ylabel('Index')
        self.plot.plot(list_i)
        self.canvas_matplot.draw()

    # Update frame
    def update_frame(self, new_heights_list, position, list_i, iterator,alpha,continu):
        self.update_modelisation(new_heights_list, position,alpha,continu)
        self.update_plot(list_i,iterator)
        self.update()
