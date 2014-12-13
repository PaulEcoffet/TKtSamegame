"""
Fichier à lancer pour jouer.

En fonction de l'option, la version graphique ou console est lancée.
Mode graphique:
```
python samegame.py
```

Mode console:
```
python samegame.py -t
```

"""

from terminal.interface import TerminalInterface
from graphique.tkinterface import TkInterface

import sys


def main_terminal():
    """Charge l'interface console"""
    interface = TerminalInterface()
    interface.run()


def main_graphique():
    """Charge l'interface Tkinter"""
    TkInterface()

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '-t':
        main_terminal()
    else:
        main_graphique()
