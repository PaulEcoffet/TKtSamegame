__author__ = 'François Gouet; Paul Ecoffet'

from game.samegame import SameGame

class Answer:
    """
    Lie une réponse à une action ou une valeur, utilisée par la fonction ask
    """
    def __init__(self, value, text):
        self.value = value
        self.text = text

class Board():
    """
    Ceci est la matrice de cases 
    """
    global char
    char = []
    col ="Z"
    char[0] = "+---"
    char[1] = "| "+col+" "
    
    
    def __init__(self,param):
        self.param = param
        mat = {}
        self.draw_Cell("Z",param[0],param[1])
                
    def createBoard(self,param):
       pass 

    def draw_Cell(self,y,nb_lines,nb_col):
        i = 0
        while i < nb_col:
            print(char[0]*nb_lines+"+")
            print(char[1]*nb_lines+"|")
            print("",end="")
            i+=1
        print(char[0]*nb_lines+"+")

        

class TerminalInterface():
    """
    Classe principale de l'interface console.
    """

    def __init__(self, game):
        self.game = game

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
        print('See ya')

    def display_main_menu(self):
        """
        Affiche le menu principal, lorsqu'on est en dehors d'une partie
        """
        actions = [
            Answer(self.new_game, 'Nouvelle partie'),
            Answer(self.load_game, 'Charger une partie'),
            Answer(self.display_help, 'Afficher l\'aide'),
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
        Demande à l'utilisateur le nombre de cases et le nombre de couleurs
        Tant que sa réponse n'est pas un entier recommencer
        """
        nombres = ['nombre ligne','nombre de colonnes','nombre de couleur']
        param = [0,0,0]
        well_answered = False
        i = 0
        while not well_answered or i != len(nombres):
            print(nombres[i])
            response = input('>')
            try:
                int_response = int(response)
            except ValueError:
                pass
            else:
                if 1 <= int_response:
                    well_answered = True
            param[i] = int_response
            i+=1
        B = Board(param)

    def load_game(self):
        pass

    def display_help(self):
        pass
