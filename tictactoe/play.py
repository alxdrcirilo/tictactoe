from copy import deepcopy

from tictactoe.board import Board
from tictactoe.logic import Logic


class Play:
    def __init__(self, size: int = 3) -> None:
        self.board = Board(size=size)
        self.logic = Logic()

    def random(self) -> None:
        while not self.board.is_over():
            x, y = self.board.get_random_move()
            self.board.move(x=x, y=y, player=self.board.player)
            self.board.player = self.board.get_next_player()

    def minimax(self, depth: int = 3) -> None:
        while not self.board.is_over():
            if self.board.player == 0:
                x, y = self.board.get_random_move()
                self.board.move(x=x, y=y, player=self.board.player)
                self.board.player = self.board.get_next_player()

            elif self.board.player == 1:
                scores = {}
                for (x, y) in self.board.get_moves():
                    self.board.move(x=x, y=y, player=self.board.player)
                    state = deepcopy(self.board)
                    score = self.logic.minimax(
                        state=state,
                        depth=depth,
                        maximizer=True,
                        player=self.board.player,
                    )
                    scores[(x, y)] = score
                    self.board.undo(x, y)

                # Get first <(x, y)> of max <score>
                x, y = max(scores, key=scores.get)
                self.board.move(x=x, y=y, player=self.board.player)
                self.board.player = self.board.get_next_player()
