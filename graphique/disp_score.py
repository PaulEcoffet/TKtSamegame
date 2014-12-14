__author__ = 'François Gouet, Paul Ecoffet'


from tkinter import *
from graphique.partieperso import PartiePerso
import pickle
import tkinter.filedialog
import os.path

class BestScoreFrame(Frame):

    def __init__(self,frame,place):
        self.bf = frame
        self.place = place
        self.new = Frame.__init__(self)
        self.new = Toplevel(self)
        self.new.title("Meilleurs scores")
        self.actu()
        self.disp()
        e =Entry(self.new)
        e.grid(row=0,column=0)
        
    def actu(self):
            pass
    def disp(self):
        f = open('score.txt','r')
        data = f.read()
        Results = Label(self.new, text = data)
        Results.grid(row = 1, column = 0)
        for i in range(10):
           line = f.readlines()
           #print(
           r = Label(self.new,text=line)
           r.grid(row=i,column =0 )

##        b=0
##        #data = f.read()
##        f.close()
##        for i in f.readlines():
##            Results = Label(self.new, text = f.readline())
##            Results.grid(row = b+1, column = 0)
