from tkinter import *

class BoardFrame(Frame):

    def __init__(self, interface, game):
        super().__init__(self.interface.root)
        self.interface = interface

        label = Label(self, text='LOOL')
        label.pack()
