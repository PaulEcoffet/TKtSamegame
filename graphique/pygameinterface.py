from tkinter import *
from graphique.menutk import MenuFrame

class PygameInterface(object):

    def __init__(self):
        self.root = Tk()
        self.frame = MenuFrame(self)
        self.frame.pack(side=LEFT, fill=BOTH, expand=YES)
        self.resize()
        self.root.title("SAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAME GAME")
        self.root.mainloop()

    def switch_frame(self, frame_cls, *args, **kwargs):
        self.frame.destroy()
        self.frame = frame_cls(self, *args, **kwargs)
        self.frame.pack(side=LEFT, fill=BOTH, expand=YES)
        self.resize()

    def switch_to_menu(self):
    	self.switch_frame(MenuFrame)

    def resize(self):
        self.root.update()
        self.root.minsize(self.root.winfo_width(),self.root.winfo_height())
        self.root.geometry("{}x{}".format(self.root.winfo_width(),self.root.winfo_height()))
        
