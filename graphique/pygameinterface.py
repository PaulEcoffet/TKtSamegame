from tkinter import *
from graphique.menutk import MenuFrame

class PygameInterface(object):

    def __init__(self):
        self.root = Tk()
        self.frame = MenuFrame(self)
        self.frame.pack(side=LEFT, fill=BOTH)
        self.root.mainloop()

    def switch_frame(self, frame_cls, *args, **kwargs):
        self.frame.destroy()
        self.frame = frame_cls(self, *args, **kwargs)
        self.frame.pack(side=LEFT, fill=BOTH)
