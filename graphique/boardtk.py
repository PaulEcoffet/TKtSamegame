__author__ = 'François Gouet, Paul Ecoffet'


from tkinter import *
import tkinter.simpledialog
from game.errors import InvalidCellError, NotEnoughCellsError
import tkinter.filedialog
import tkinter.messagebox
import pickle
from game.highscores import Highscores

from PIL import ImageTk


class BoardFrame(Frame):
    """
    Board frame
    """
    def __init__(self, interface, game):
        super().__init__(interface.root)
        self.possible = {"B": ImageTk.PhotoImage(file="graphique/img/blue.png"),
                         "O": ImageTk.PhotoImage(file="graphique/img/orange.png"),
                         "A": ImageTk.PhotoImage(file="graphique/img/blurple.png"),
                         "M": ImageTk.PhotoImage(file="graphique/img/yellow.png"),
                         "V": ImageTk.PhotoImage(file="graphique/img/green.png"),
                         "R": ImageTk.PhotoImage(file="graphique/img/red.png"),
                         " ": PhotoImage(file="graphique/img/blank_big.gif")}
        self.hover = {"B": ImageTk.PhotoImage(file="graphique/img/blue_h.png"),
                      "O": ImageTk.PhotoImage(file="graphique/img/orange_h.png"),
                      "A": ImageTk.PhotoImage(file="graphique/img/blurple_h.png"),
                      "M": ImageTk.PhotoImage(file="graphique/img/yellow_h.png"),
                      "V": ImageTk.PhotoImage(file="graphique/img/green_h.png"),
                      "R": ImageTk.PhotoImage(file="graphique/img/red_h.png"),
                      " ": PhotoImage(file="graphique/img/blank_big.gif")}
        self.interface = interface
        self.game = game
        self.highlighted_cells = []
        self.buttons = []
        self.score_saved = False
        board = Frame(self, relief=SOLID, bg='black', border=2)
        self.gen_board(board)
        self.disp_board()

        messageframe = Frame(self, borderwidth=2)
        self.score = Label(messageframe,
                           text="SCORE : " + str(self.game.score),
                           borderwidth=2, relief=GROOVE)
        self.score.grid(column=0, row=0, sticky='nswe')
        messageframe.columnconfigure(0, weight=1, uniform='messageframe')
        self.message = Label(messageframe, text='', fg='red',
                             borderwidth=2, relief=GROOVE)
        self.message.grid(column=1, row=0, sticky='nswe')
        messageframe.columnconfigure(1, weight=1, uniform='messageframe')
        messageframe.pack(side=TOP, padx=5, pady=5, expand=True, fill=BOTH)

        board.pack(side=TOP, padx=5, pady=5, expand=True, fill=BOTH)

        bottom_frame = Frame(self)
        bottom_frame.pack(side=TOP, fill=BOTH)
        back_to_menu_button = Button(bottom_frame, text='Retour menu',
                                     command=self.back_to_menu)
        back_to_menu_button.pack(side=RIGHT, padx=5, pady=5)
        self.save_game_button = Button(bottom_frame, text='Sauvegarder',
                                       command=self.save)
        self.save_game_button.pack(side=LEFT, padx=5, pady=5)

    def save(self):
        """
        Affiche une fenêtre pour sauvegarder la partie.
        """
        if not self.game.can_play:
            tkinter.messagebox.showerror('Impossible de sauvegarder',
                                         'Vous ne pouvez pas sauvegarder une partie terminée')
            return
        savefile = tkinter.filedialog.asksaveasfile(mode='wb', initialdir='../saves',
                                                    defaultextension='.samegame')
        if savefile:
            try:
                pickle.dump(self.game, savefile)
            except pickle.PicklingError:
                tkinter.messagebox.showerror('Sauvegarde échouée',
                                             'Impossible de sauvegarder votre partie')
            else:
                self.message['text'] = 'Partie sauvegardée #SWAG'

    def back_to_menu(self):
        """
        Change l'interface pour afficher l'écran de menu
        """
        self.interface.switch_to_menu()

    def cb_cell(self, line, col):
        """
        callback lors du clic sur une cellule.

        Clique sur la case dans la logique du jeu et met à jour le tableau.
        """
        try:
            self.game.click_on_cell(line, col)
        except InvalidCellError:
            self.message['text'] = 'Case vide'
        except NotEnoughCellsError:
            self.message['text'] = 'Pas assez de cases'
        else:
            self.message['text'] = ''
        self.disp_board()
        self.score['text'] = 'SCORE : ' + str(self.game.score)
        if not self.game.can_play:
            self.deactivate_save()
            if self.game.won:
                self.message['text'] = "FELICITATION"
            elif not self.game.can_play:
                self.message['text'] = "PARTIE FINIE"
            self.save_score()
        self.hover_cell(line, col)

    def deactivate_save(self):
        """
        Désactive le bouton de sauvegarde.

        Appelée quand la partie est finie.
        """
        self.save_game_button['state'] = DISABLED

    def hover_cell(self, line, col):
        """
        Surligne la cellule et les cellules de même couleur voisines.

        Appelée lorsque le curseur est au dessus d'une cellule.
        """
        self.clear_highlighted()
        to_highlight = self.game.get_same_nearby(line, col)
        for i, j in to_highlight:
            self.buttons[i][j]['image'] = self.hover[self.game.board[i][j]]
        self.highlighted_cells = to_highlight

    def clear_highlighted(self):
        """
        Supprime les cellules actuellement surlignées.
        """
        for i, j in self.highlighted_cells:
            self.buttons[i][j]['image'] = self.possible[self.game.board[i][j]]
        self.highlighted_cells = []

    def disp_board(self):
        """
        Met à jour le tableau depuis la logique du jeu.
        """
        for line in range(self.game.nb_line):
            for col in range(self.game.nb_col):
                self.buttons[line][col]['image'] = self.possible[self.game.board[line][col]]

    def gen_board(self, board):
        """
        Génère le plateau.
        """
        if self.buttons:  # S'il y a des boutons, on nettoie
            for line in self.buttons:
                for button in line:
                    button.destroy()
        self.buttons = []
        for line in range(self.game.nb_line):
            self.buttons.append([])
            for col in range(self.game.nb_col):
                button = Button(board, borderwidth=0, bg='black',
                                activebackground='black', relief=FLAT, padx=0, pady=0,
                                command=lambda line=line, col=col: self.cb_cell(line, col))
                button.bind('<Enter>', lambda event, line=line, col=col: self.hover_cell(line, col))
                button.bind('<Leave>', lambda event: self.clear_highlighted())
                self.buttons[line].append(button)
                button.grid(column=col, row=line)

    def save_score(self):
        highscores = Highscores('high.scores')
        name = tkinter.simpledialog.askstring(
            'Score', 'Veuillez entrer votre nom pour le classement')
        if not name:
            name = 'Anonyme'
        highscores.add_score(name, self.game)
