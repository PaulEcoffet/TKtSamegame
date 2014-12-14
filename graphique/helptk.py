from tkinter import *


class HelpWindow(Toplevel):
    """
    Affiche une fenêtre contenant l'aide du jeu
    """
    def __init__(self):
        super().__init__()
        button = Button(self, text='Fermer', command=self.destroy)
        button.pack(side=BOTTOM, pady=2, expand=True)
        frame = Frame(self)
        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill=Y)

        with open('help.txt', 'r') as content_file:
            content = content_file.read()
        text = Text(frame, wrap=WORD, yscrollcommand=scrollbar.set)
        text.insert(END, content)
        text['state'] = DISABLED
        text.pack(expand=True, fill=BOTH)
        frame.pack(expand=True, fill=BOTH)
        scrollbar.config(command=text.yview)
