__author__ = 'François Gouet, Paul Ecoffet'


from tkinter import *
from graphique.partieperso import PartiePerso
import pickle
import tkinter.filedialog
import os.path

class BestScoreFrame(Frame):

    def __init__(self,menuFrame):
        self.mf = menuFrame
        new = Frame.__init__(self)
        new = Toplevel(self)
        new.title("Meilleurs scores")
##        print("------------------------------------------------------------")
##        SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
##        print("example 1: "+SITE_ROOT)
##        PARENT_ROOT=os.path.abspath(os.path.join(SITE_ROOT, os.pardir))
##        print("example 2: "+PARENT_ROOT)
##        GRANDPAPA_ROOT=os.path.abspath(os.path.join(PARENT_ROOT, os.pardir))
##        print("example 3: "+GRANDPAPA_ROOT)
##        print ("------------------------------------------------------------")
        f = open('score.txt','r')
        #print(f)
        #print(f.read())
        #print(f.readline())
        b=0
        data = f.read()
        f.close()
        Results = Label(new, text = data)
        Results.grid(row = 1, column = 1)
    
