from tkinter import *
from game.errors import InvalidCellError, NotEnoughCellsError
import tkinter.filedialog
import tkinter.messagebox
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
        self.hover = {"B":ImageTk.PhotoImage(file="graphique/img/blue_h.png"),
                      "O":ImageTk.PhotoImage(file="graphique/img/orange_h.png"),
                      "A":ImageTk.PhotoImage(file="graphique/img/blurple_h.png"),
                      "M":ImageTk.PhotoImage(file="graphique/img/yellow_h.png"),
                      "V":ImageTk.PhotoImage(file="graphique/img/green_h.png"),
                      "R":ImageTk.PhotoImage(file="graphique/img/red_h.png"),
                      " ": PhotoImage(file="graphique/img/blank_big.gif")}
        self.interface = interface
        self.game = game
        self.highlighted_cells = []
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
        if not self.game.can_play:
            tkinter.messagebox.showerror('Impossible de sauvegarder', 'Vous ne pouvez pas sauvegarder une partie terminée')
            return
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
            self.deactivate_save()
        elif not self.game.can_play:
            self.message['text'] = "PARTIE FINIE"
            self.deactivate_save()
        self.score['text'] = 'SCORE: ' + str(self.game.score)

    def deactivate_save(self):
        self.save_game_button['state'] = DISABLED

    def hover_cell(self, line, col):
        self.clear_highlighted()
        to_highlight = self.game.get_same_nearby(line, col)
        for i, j in to_highlight:
            self.buttons[i][j]['image'] = self.hover[self.game.board[i][j]]
        self.highlighted_cells = to_highlight


    def clear_highlighted(self):
        for i, j in self.highlighted_cells:
            self.buttons[i][j]['image'] = self.possible[self.game.board[i][j]]
        self.highlighted_cells = []


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
                c.bind('<Enter>', lambda event, line=line, col=col: self.hover_cell(line, col))
                c.bind('<Leave>', lambda event: self.clear_highlighted())
                self.buttons[line].append(c)
                c.grid(column=col, row=line)
