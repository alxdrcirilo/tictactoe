from math import inf

from tictactoe.board import Board


class Logic:
    def __init__(self) -> None:
        self.win = 1
        self.loss = -1
        self.draw = 0

    def get_score(self, state, player) -> int:
        if state.is_over():
            if state.winner == player:
                return self.win
            elif state.winner == None:
                return self.draw
            else:
                return self.loss
        else:
            return 0

    def minimax(self, state: Board, depth: int, maximizer: bool, player: int) -> float:
        if depth == 0 or state.is_over():
            score = self.get_score(state=state, player=player)
            return score

        if maximizer:
            val = -inf
            for (x, y) in state.get_moves():
                state.move(x=x, y=y, player=state.player)
                state.player = state.get_next_player()
                val = max(val, self.minimax(state, depth - 1, False, player))
            return val

        else:
            val = inf
            for (x, y) in state.get_moves():
                state.move(x=x, y=y, player=state.player)
                state.player = state.get_next_player()
                val = min(val, self.minimax(state, depth - 1, True, player))
            return val
