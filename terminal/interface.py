"""
Ce module contient l'interface utilisateur en console du samegame
"""
__author__ = 'François Gouet, Paul Ecoffet'

from game.samegame import SameGame
from terminal.errors import InterfaceInputError
from game.errors import NotEnoughCellsError, InvalidCellError
import string
import pickle
import glob
from game.highscores import Highscores


class Answer:
    """
    Lie une réponse à une action ou une valeur, utilisée par la fonction ask
    """
    def __init__(self, value, text):
        self.value = value
        self.text = text


class TerminalInterface():
    """
    Classe principale de l'interface console.
    """

    def __init__(self):
        self.game = None

    def run(self):
        """
        Démarre l'interface du SameGame en mode console, c'est la seule fonction
        qui doit être lancer en dehors de cette classe, en général par le main
        """
        run = True
        self.welcome()
        while run:
            run = self.display_main_menu()
        self.goodbye()

    def welcome(self):
        """
        Accueille le joueur
        """
        print("="*80)
        print("Bienvenue dans l'ultimate SameGame".center(80))
        print("="*80)
        print("Conçu par Paul Ecoffet et François Gouet".rjust(80))
        print()

    def goodbye(self):
        """
        Affiche un message d'au revoir
        """
        print("Merci d'avoir joué. À la prochaine !")

    def display_main_menu(self):
        """
        Affiche le menu principal, lorsqu'on est en dehors d'une partie
        """
        actions = [
            Answer(self.new_game, 'Nouvelle partie'),
            Answer(self.load_game, 'Charger une partie'),
            Answer(self.display_help, 'Afficher l\'aide'),
            Answer(self.list_scores, 'Regarder les meilleurs scores'),
            Answer('quit', 'Quitter')
        ]
        answer = self.ask('Que souhaitez-vous faire ?', actions)
        if answer == 'quit':
            return False
        else:
            answer()
        return True

    def ask(self, question, answers):
        """
        Propose à l'utilisateur de choisir un item parmi une liste de choix.

        ask s'occupe de s'assurer que l'entrée utilisateur est valide et
        continue de demander tant que ce n'est pas le cas
        """
        well_answered = False
        while not well_answered:
            print(question)
            for i, action in enumerate(answers):
                print("{}: {}".format(i + 1, action.text))
            response = input('> ')
            try:
                int_response = int(response)
            except ValueError:
                pass
            else:
                if 1 <= int_response <= len(answers):
                    well_answered = True
        return answers[int_response - 1].value

    def new_game(self):
        """
        demande à l'utilisateur sa configuration et lance une nouvelle partie.
        """
        nb_line, nb_col, nb_colors = self.ask_set_up_game()
        self.game = SameGame(nb_col, nb_line, nb_colors)
        self.run_game()

    def run_game(self):
        """
        Fait tourner une partie jusqu'à ce qu'elle prenne fin
        """
        quit_game = False
        while self.game.not_finished and not quit_game:
            self.disp_board()
            print("score: {}".format(self.game.score))
            entry = input('Enter cell > ').upper()
            try:
                line, col = self.cell_choice(entry)
            except InterfaceInputError:
                if entry == 'QUIT' or entry == 'EXIT':
                    quit_game = True
                elif entry == 'SAVE':
                    path = input('nom du fichier >')
                    self.save_game(path)
                else:
                    print("Case entrée invalide")
            else:
                try:
                    self.game.click_on_cell(line, col)
                except NotEnoughCellsError:
                    print("pas assez de cases")
                except InvalidCellError:
                    print("Vous ne pouvez supprimer une case vide")
        self.disp_board()
        print("score: {}".format(self.game.score))
        if not quit_game:
            if self.game.won:
                print("Impressionnant")
            else:
                print("Dommage")
            self.save_score()

    def cell_choice(self, choice):
        """
        Retourne l'index de la cellule si valide, ou lance une exception sinon
        """
        col = ord(choice[0]) - ord('A')
        try:
            line = int(choice[1:])-1
        except ValueError:
            raise InterfaceInputError()
        if 0 <= col < self.game.nb_col and 0 <= line < self.game.nb_line:
            return line, col
        else:
            raise InterfaceInputError()

    def disp_board(self):
        """Affiche le tableau"""
        table = "   "
        for valeur in string.ascii_uppercase[:self.game.nb_col]:
            table += "  " + valeur + " "
        table += "\n"
        for i, line in enumerate(self.game.board):
            table += "   +" + "---+" * self.game.nb_col + '\n'
            table += "{:2d} | ".format(i+1)
            for cell in line:
                table += cell + " | "
            table += str(i+1) + "\n"
        table += "   +" + "---+" * self.game.nb_col + "   \n"
        table += '   '
        for valeur in string.ascii_uppercase[:self.game.nb_col]:
            table += "  "+valeur+" "
        print(table)

    def ask_set_up_game(self):
        """
        Demande à l'utilisateur le nombre de cases et le nombre de couleurs
        Tant que sa réponse n'est pas un entier recommencer
        """
        nombres = ['Combien de lignes', 'Combien de colonnes', 'Combien de couleurs']
        param = [0, 0, 0]
        contraintes = [(6, 12), (6, 12), (2, 6)]
        well_answered = False
        i = 0
        while not well_answered or i != len(nombres):
            print('{} (entre {} et {})'.format(nombres[i], contraintes[i][0],
                                               contraintes[i][1]))
            response = input('> ')
            try:
                int_response = int(response)
            except ValueError:
                pass
            else:
                if contraintes[i][0] <= int_response <= contraintes[i][1]:
                    well_answered = True
                    param[i] = int_response
                    i += 1
        return param

    def load_game(self):
        """
        Affiche l'interface pour charger une partie et lance la partie select
        """
        actions = [Answer(name, name) for name in glob.glob("saves/*.samegame")]
        if actions:
            actions.append(Answer(None, '*Ne pas charger de partie*'))
            f_path = self.ask("Quelle partie voulez-vous charger ?", actions)
            if f_path:
                with open(f_path, 'rb') as save:
                    self.game = pickle.load(save)
                self.run_game()
        else:
            print("Il n'y a pas de parties à charger")

    def save_game(self, path):
        """
        Sauvegarde la partie actuelle dans un fichier `path`.samegame
        """
        with open('saves/' + path + '.samegame', "wb") as save:
            pickle.dump(self.game, save)

    def display_help(self):
        """
        Affiche l'aide du jeu.
        """
        with open("help.txt") as help_file:
            print(help_file.read())

    def save_score(self):
        """
        Enregistre le score du joueur
        """
        highscores = Highscores('high.scores')
        name = input('Veuillez entrer votre nom : ')
        highscores.add_score(name, self.game)

    def list_scores(self):
        """Affiche les meilleurs scores"""
        highscores = Highscores('high.scores')
        print('Veuillez entrer la catégorie de score :')
        param = self.ask_set_up_game()
        scores = highscores.get_scores(*param)
        print('*'*70)
        if scores:
            for i, score in enumerate(scores[:10]):
                print(i+1, ':', score[0], '(', score[1], ')')
        else:
            print('Pas de score pour cette catégorie')
        print('*'*70)
        print()
