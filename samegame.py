from terminal.interface import TerminalInterface
from graphique.pygameinterface import PygameInterface
from game.samegame import SameGame

import sys


def main_terminal():
    interface = TerminalInterface()
    interface.run()

def main_graphique():
    PygameInterface()

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '-t':
        main_terminal()
    else:
        main_graphique()
