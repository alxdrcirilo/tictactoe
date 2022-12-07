from tictactoe.play import Play
from tictactoe.tournament import Tournament

if __name__ == "__main__":
    # Random play
    game = Play()
    game.random()

    # Tournament
    arena = Tournament(sizes=range(3, 4), depths=range(1, 2), n=range(3))
    arena.play()
