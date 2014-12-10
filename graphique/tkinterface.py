from tkinter import *
from graphique.menutk import MenuFrame

class TkInterface(object):

    def __init__(self):
        self.root = Tk()
        self.frame = MenuFrame(self)
        self.frame.pack(side=LEFT, fill=BOTH, expand=True)
        self.resize()
        self.root.resizable(False, False)
        self.root.mainloop()

    def switch_frame(self, frame_cls, *args, **kwargs):
        self.frame.destroy()
        self.frame = frame_cls(self, *args, **kwargs)
        self.frame.pack(side=LEFT, fill=BOTH, expand=True)
        self.resize()

    def switch_to_menu(self):
    	self.switch_frame(MenuFrame)

    def resize(self):
        self.root.update()
        self.root.wm_geometry("{}x{}".format(self.root.winfo_reqwidth(), self.root.winfo_reqheight()))
