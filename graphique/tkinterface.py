__author__ = 'François Gouet, Paul Ecoffet'


from tkinter import *
from graphique.menutk import MenuFrame


class TkInterface(object):
    """
    Classe principale de l'interface Tkinter

    Cette interface charge des écrans (des objets Frame) en fonction
    du contexte.
    """
    def __init__(self):
        self.root = Tk()
        self.frame = MenuFrame(self)
        self.frame.pack(side=LEFT, fill=BOTH, expand=True)
        self.resize()
        self.root.resizable(False, False)
        self.root.title('SameGame')
        self.root.mainloop()

    def switch_frame(self, frame_cls, *args, **kwargs):
        """
        Affiche un nouvel écran de la classe `frame_cls`.

        Il est possible d'ajouter des arguments à pour l'instanciation du
        nouvel écran à l'aide de *args et **kwargs
        """
        self.frame.destroy()
        self.frame = frame_cls(self, *args, **kwargs)
        self.frame.pack(side=LEFT, fill=BOTH, expand=True)
        self.resize()

    def switch_to_menu(self):
        """
        Ramène au menu principal
        """
        self.switch_frame(MenuFrame)

    def resize(self):
        """
        Redimensionne la fenêtre pour que tous les widgets puissent tenir
        """
        self.root.update()
        self.root.wm_geometry("{}x{}".format(self.root.winfo_reqwidth(),
                                             self.root.winfo_reqheight()))
