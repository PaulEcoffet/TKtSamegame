from tkinter import *

class BoardFrame(Frame):
    def __init__(self, interface, game):
        super().__init__(interface.root)
        self.possible = {"B":"graphique/img/ZB.gif","O":"graphique/img/ZC.gif","A":"graphique/img/ZG.gif",
                                "M":"graphique/img/ZM.gif", "V":"graphique/img/ZY.gif",
                                "R":"graphique/img/ZR.gif"}
        b = self.possible
        self.grid = {}
        self.interface = interface
        self.game = game
        for loop in range(self.game.nb_col*self.game.nb_line):
            col = loop % self.game.nb_col
            line = loop // self.game.nb_line
            img = PhotoImage(file= b[self.game.board[line][col]])
            c = Button(self,image = img)
            c.image = img
            c.grid(column=col, row=line, ipadx=5, ipady=5)
        
    

    
