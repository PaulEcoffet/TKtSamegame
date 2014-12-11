from tkinter import *
from game.samegame import SameGame
from graphique.boardtk import BoardFrame
import pickle
import tkinter.filedialog

class MenuFrame(Frame):

    def __init__(self,interface):
        self.interface = interface
        super().__init__(interface.root)
        for i in range(3):
            self.grid_columnconfigure(i,weight = 2,minsize=10)
            self.grid_rowconfigure(i,weight = 2,minsize=10)
        img = PhotoImage(file="graphique/img/beaugosse.gif")
        lab_img = Label(self,image=img)
        lab_img.image = img
        lab_img.grid(row=0,column=0,columnspan=3)

        nb_line_label=Label(self,text="Nombre de lignes")
        nb_line_label.grid(row=1,column=0,sticky='NSWE')
        slider_color = Scale(self, orient= HORIZONTAL,from_=6, to=12,
                             command=self.set_nb_line)
        slider_color.grid(row=1,column=1,sticky=W+N+S+E)

        nb_col_label=Label(self,text="Nombre de colonnes")
        nb_col_label.grid(row=2,column=0,sticky=W+N+S+E)
        slider_nb_col = Scale(self, orient= HORIZONTAL,from_=6, to=12,
                             command=self.set_nb_col)
        slider_nb_col.grid(row=2,column=1,sticky=W+N+S+E)

        nb_color_label=Label(self,text="Nombre de couleurs")
        nb_color_label.grid(row=3,column=0,sticky=W+N+S+E)
        slider_nb_line = Scale(self, orient= HORIZONTAL,from_=2, to=len(SameGame.possible_colors),
                             command=self.set_nb_color)
        slider_nb_line.grid(row=3,column=1,sticky=W+N+S+E)

        new_game_button = Button(self,text="NOUVELLE PARTIE",command=self.new_game)
        new_game_button.grid(row=4,column=0,columnspan=2,sticky=W+N+S+E)
        load_button = Button(self,text="CHARGER UNE PARTIE",command=self.load_game)
        load_button.grid(row=3,column=2,sticky=W+N+S+E)
        load_button = Button(self,text="AIDE",command=self.help)
        load_button.grid(row=2,column=2,sticky=W+N+S+E)

    def new_game(self):
        game = SameGame()
        game.new_game(self.nb_line,self.nb_col,self.nb_colors)
        self.interface.switch_frame(BoardFrame,game)

    def load_game(self):
        try:
            f = tkinter.filedialog.askopenfile(mode='rb', initialdir = 'saves/')
            game = pickle.load(f)
        except Exception as e:
            print(e) # Show error
        else:
            if isinstance(game, SameGame):
                self.interface.switch_frame(BoardFrame, game)

    def set_nb_col(self,n):
        self.nb_col = int(n)
    def set_nb_color(self,n):
        self.nb_colors = int(n)
    def set_nb_line(self,n):
        self.nb_line = int(n)
    def help(self):
        pass
