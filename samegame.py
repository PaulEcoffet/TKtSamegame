from terminal.interface import TerminalInterface
from graphique.pygameinterface import PygameInterface
from game.samegame import SameGame

def main_terminal():
    interface = TerminalInterface()
    interface.run()

def main_graphique():
    PygameInterface()

if __name__ == '__main__':
    main_terminal()
