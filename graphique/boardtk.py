from tkinter import *
from game.errors import InvalidCellError, NotEnoughCellsError



class BoardFrame(Frame):

    def __init__(self, interface, game):
        super().__init__(interface.root)
        self.possible = {"B":PhotoImage(file="graphique/img/ZB.gif"),
                         "O":PhotoImage(file="graphique/img/ZC.gif"),
                         "A":PhotoImage(file="graphique/img/ZG.gif"),
                         "M":PhotoImage(file="graphique/img/ZM.gif"),
                         "V":PhotoImage(file="graphique/img/ZY.gif"),
                         "R":PhotoImage(file="graphique/img/ZR.gif"),
                         " ": PhotoImage(width=48, height=48)}
        self.grid = {}
        self.interface = interface
        self.game = game
        self.buttons = []
        self.board = Frame(self, relief=SOLID, border=2)
        self.board.pack(side=TOP, padx=5, pady=5)
        self.gen_buttons()
        self.dispBoard()
        self.score = Label(self, text="SCORE :" + str(self.game.score))
        self.score.pack(side=TOP)
        self.message = Label(self, text='', fg='red')
        self.message.pack(side=TOP)




    def cb_cell(self,cell):
        try:
            self.game.click_on_cell(cell[1],cell[0])
        except InvalidCellError as e:
            self.message['text'] = str(e)
        except  NotEnoughCellsError as e:
            self.message['text'] = 'Pas assez de cases de même couleur'
        else:
            self.message['text'] = ''
        self.dispBoard()
        if self.game.won:
            self.score['text'] = "FELICITATION SCORE:" + str(self.game.score)
        elif not self.game.can_play:
            self.score['text'] = "PARTIE FINIE SCORE:" + str(self.game.score)
        else:
            self.score['text'] = 'SCORE: ' + str(self.game.score)


    def dispBoard(self):
        for loop in range(self.game.nb_col*self.game.nb_line):
            col = loop % self.game.nb_col
            line = loop // self.game.nb_line
            self.buttons[line][col]['image'] = self.possible[self.game.board[line][col]]

    def gen_buttons(self):
        if self.buttons:  # S'il y a des boutons, on nettoie
            for line in self.buttons:
                for button in line:
                    button.destroy()
        self.buttons = []
        for line in range(self.game.nb_line):
            self.buttons.append([])
            for col in range(self.game.nb_col):
                c = Button(self.board,command=lambda cell=(col,line): self.cb_cell(cell))
                self.buttons[line].append(c)
                c.grid(column=col, row=line)
