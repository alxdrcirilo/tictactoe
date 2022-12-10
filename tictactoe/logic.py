from copy import deepcopy
from math import inf

from tictactoe.board import Board


class Logic:
    def __init__(self) -> None:
        self.win = 10
        self.loss = -10
        self.draw = 0

    def get_score(self, state: Board, player: int) -> int:
        if state.is_over():
            if state.winner == player:
                return self.win
            elif state.winner == None:
                return self.draw
            else:
                return self.loss
        else:
            return 0

    def minimax(
        self,
        state: Board,
        depth: int,
        maximizer: bool,
        player: int,
        a: float | None = None,
        b: float | None = None,
    ) -> tuple[tuple[int, int], float]:
        if depth == 0 or state.is_over():
            score = self.get_score(state=state, player=player)
            return None, score

        best_move = state.get_moves()[0]

        if maximizer:
            best_score = -inf
            for (x, y) in state.get_moves():
                state_copy = deepcopy(state)
                state_copy.move(x=x, y=y, player=state_copy.player)
                state_copy.player = state_copy.get_next_player()

                score = self.minimax(state_copy, depth - 1, False, player, a, b)[1]
                if score > best_score:
                    best_score = score
                    best_move = (x, y)

                if a and b:
                    a = max(a, score)
                    if a >= b:
                        break

            return best_move, best_score

        else:
            best_score = inf
            for (x, y) in state.get_moves():
                state_copy = deepcopy(state)
                state_copy.move(x=x, y=y, player=state_copy.player)
                state_copy.player = state_copy.get_next_player()

                score = self.minimax(state_copy, depth - 1, True, player, a, b)[1]

                if score < best_score:
                    best_score = score
                    best_move = (x, y)

                if a and b:
                    b = min(b, score)
                    if a >= b:
                        break

            return best_move, best_score
