from terminal.interface import TerminalInterface
from graphique.pygameinterface import PygameInterface
from game.samegame import SameGame

def main_terminal():
    game = SameGame()
    interface = TerminalInterface(game)
    interface.run()

def main_graphique():
    PygameInterface()

if __name__ == '__main__':
    main_graphique()
