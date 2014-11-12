from terminal.interface import TerminalInterface
from game.samegame import SameGame

def main():
    game = SameGame()
    interface = TerminalInterface(game) 
    interface.run()
1
if __name__ == '__main__':
    main()
