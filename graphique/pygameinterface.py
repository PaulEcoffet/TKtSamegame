from tkinter import *
from graphique.menutk import MenuFrame

class PygameInterface(object):

    def __init__(self):
        self.root = Tk()
        frame = MenuFrame(self.root)
        frame.pack(side=LEFT, fill=BOTH)
        self.root.mainloop()


        
        
        
