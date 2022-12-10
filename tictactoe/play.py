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

    def minimax(
        self, depth: int = 3, alpha: float | None = None, beta: float | None = None
    ) -> None:
        while not self.board.is_over():
            if self.board.player == 0:
                x, y = self.board.get_random_move()
                self.board.move(x=x, y=y, player=self.board.player)
                self.board.player = self.board.get_next_player()

            elif self.board.player == 1:
                x, y = self.logic.minimax(
                    state=self.board,
                    depth=depth,
                    maximizer=True,
                    player=self.board.player,
                    a=alpha,
                    b=beta,
                )[0]
                self.board.move(x=x, y=y, player=self.board.player)
                self.board.player = self.board.get_next_player()
