from terminal.interface import TerminalInterface
from graphique.tkinterface import TkInterface
from game.samegame import SameGame

import sys


def main_terminal():
    interface = TerminalInterface()
    interface.run()

def main_graphique():
    TkInterface()

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argvv[1] == '-t':
        main_terminalminal()
    else:
        main_graphique()
