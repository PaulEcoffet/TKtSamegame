from terminal.interface import TerminalInterface
from game.samegame import SameGame

def main():
    game = SameGame()
    interface = TerminalInterface(game)
    interface.run()

if __name__ == '__main__':
    main()
