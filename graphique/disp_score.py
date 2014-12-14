__author__ = 'François Gouet, Paul Ecoffet'

from tkinter import *
import pickle
import tkinter.filedialog
import os.path
from game.highscores import Highscores

class BestScoreFrame(Toplevel):

    def __init__(self,game):
        super().__init__()
        self.game = game
        self.title("Meilleurs scores")
        self.highscores = Highscores('high.scores')
        self.e = Entry(self)
        self.e.grid(row=0,column=0)
        self.b = Button(self,command=self.save)
        self.b.grid(row=1,column=0)

    def save(self):
        var = self.e.get()
        self.a = Label(self,text=var)
        self.a.grid(row=2,column=0)
        self.highscores.add_score(var,self.game)
        self.destroy()
