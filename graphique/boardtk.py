from tkinter import *
from game.errors import InvalidCellError, NotEnoughCellsError
import tkinter.filedialog
import pickle

from PIL import ImageTk


class BoardFrame(Frame):

    def __init__(self, interface, game):
        super().__init__(interface.root)
        self.possible = {"B":ImageTk.PhotoImage(file="graphique/img/blue.png"),
                         "O":ImageTk.PhotoImage(file="graphique/img/orange.png"),
                         "A":ImageTk.PhotoImage(file="graphique/img/blurple.png"),
                         "M":ImageTk.PhotoImage(file="graphique/img/yellow.png"),
                         "V":ImageTk.PhotoImage(file="graphique/img/green.png"),
                         "R":ImageTk.PhotoImage(file="graphique/img/red.png"),
                         " ": PhotoImage(file="graphique/img/blank_big.gif")}
        self.interface = interface
        self.game = game
        self.buttons = []
        self.board = Frame(self, relief=SOLID, bg='black', border=2)
        self.gen_buttons()
        self.dispBoard()
        self.board.pack(side=TOP, padx=5, pady=5)
        self.score = Label(self, text="SCORE :" + str(self.game.score))
        self.score.pack(side=TOP)
        self.message = Label(self, text='', fg='red')
        self.message.pack(side=TOP)

        self.bottom_frame = Frame(self)
        self.bottom_frame.pack(side=TOP, fill=BOTH)

        self.back_to_menu_button = Button(self.bottom_frame, text='Retour menu', command=self.back_to_menu)
        self.back_to_menu_button.pack(side=RIGHT)

        self.save_game_button = Button(self.bottom_frame, text='Sauvegarder', command=self.save)
        self.save_game_button.pack(side=LEFT)

    def save(self):
        f = tkinter.filedialog.asksaveasfile(mode='wb', initialdir='../saves', defaultextension='.samegame')
        try:
            pickle.dump(self.game, f)
        except TypeError as e:
            pass
        else:
            self.message['text'] = 'Partie sauvegardée #SWAG'

    def back_to_menu(self):
        self.interface.switch_to_menu()

    def cb_cell(self,cell):
        try:
            self.game.click_on_cell(cell[0],cell[1])
        except InvalidCellError as e:
            self.message['text'] = str(e)
        except  NotEnoughCellsError as e:
            self.message['text'] = 'Pas assez de cases de même couleur'
        else:
            self.message['text'] = ''
        self.dispBoard()

        if self.game.won:   
            self.message['text'] = "FELICITATION"
        elif not self.game.can_play:
            self.message['text'] = "PARTIE FINIE"
        self.score['text'] = 'SCORE: ' + str(self.game.score)


    def dispBoard(self):
        for line in range(self.game.nb_line):
            for col in range(self.game.nb_col):
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
                c = Button(self.board, borderwidth=0, bg='black', activebackground='black', relief=FLAT, padx=0, pady=0, command=lambda cell=(line,col): self.cb_cell(cell))
                self.buttons[line].append(c)
                c.grid(column=col, row=line)