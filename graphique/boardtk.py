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
        self.board = Frame(self, relief=SOLID, border=2)
        self.board.pack(side=TOP, padx=5, pady=5)
        self.dispBoard()
        self.label = Label(self, text="SCORE :" + str(self.game.score))
        self.label.pack()

        
        

    def cb_cell(self,cell):
        while self.game.can_play and self.game.not_finished:
            self.game.click_on_cell(cell[1],cell[0])
            self.dispBoard()
        if self.game.won:
            self.label['text'] = "FELICITATION SCORE:" + str(self.game.score)
        else:
            self.label['text'] = "PARTIE FINIE SCORE:" + str(self.game.score)
            

    def dispBoard(self):
        for loop in range(self.game.nb_col*self.game.nb_line):
            col = loop % self.game.nb_col
            line = loop // self.game.nb_line
            if self.game.board[line][col] == ' ':
                img = PhotoImage(width=50,height=50)
            else:
                img = PhotoImage(file= self.possible[self.game.board[line][col]])
                print(img.width())
            c = Button(self.board,image = img,command=lambda cell=(col,line): self.cb_cell(cell))
            c.image = img
            c.grid(column=col, row=line, ipadx=5, ipady=5)

    
