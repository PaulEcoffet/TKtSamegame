from tkinter import *

class BoardFrame(Frame):

    def __init__(self, interface, game):
        super().__init__(interface.root)
        self.interface = interface
        self.game = game
       # for i in range (len(UnicodeTra
        label = Label(self, text='LOOL')
        label.pack()
