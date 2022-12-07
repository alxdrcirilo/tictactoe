from random import choice

import numpy as np


class Board:
    """
    Tic-tac-toe board class.
    Contains the state of the board and basic methods.
    """

    def __init__(self, starter: int = 0, fill: int = 2, size: int = 3) -> None:
        """
        Initializes the board.

        :param starter: starting player (default: 0)
        :param fill: board state empty value (default: 2)
        """
        self.fill = fill
        self.mapping = {0: "O", 1: "X", 2: " "}

        self._state = np.full(shape=(size, size), fill_value=self.fill, dtype=np.int8)
        self._player = starter
        self._winner = None
        self._hash = hash(str(self._state))

    def __str__(self) -> str:
        """
        Returns a human-readable representation of the board.
        """
        array = np.array2string(self.state)
        for k, v in self.mapping.items():
            array = array.replace(str(k), v)
        return array

    @property
    def state(self) -> np.ndarray:
        return self._state

    @state.setter
    def state(self, values: tuple) -> None:
        x, y, player = values
        self._state[x, y] = player

    @property
    def player(self) -> int:
        return self._player

    @player.setter
    def player(self, value: int) -> None:
        self._player = value

    @property
    def winner(self) -> int | None:
        return self._winner

    @winner.setter
    def winner(self, id: int | None) -> int | None:
        self._winner = id

    @property
    def hash(self) -> int:
        """
        Returns the hash value of a given board state.
        """
        return hash(str(self._state))

    def get_next_player(self) -> int:
        """
        Returns the next player.
        """
        # TODO: improve
        players = [0, 1]
        players.remove(self.player)
        return players[0]

    def is_over(self) -> bool | tuple[bool, int]:
        """
        Checks if the game is over for both players:
        row-wise, column-wise, and on each diagonal.
        Also checks if the game reaches a draw.
        """
        # Check both players
        for player in [0, 1]:

            # Check diagonals
            diag1 = self._state.diagonal()
            diag2 = np.fliplr(self._state).diagonal()
            if np.all(diag1 == player) or np.all(diag2 == player):
                self.winner = player
                return True

            # Check row-wise (0) and column-wise(1)
            for ax in [0, 1]:
                if np.all(self._state == player, axis=ax).any():
                    self.winner = player
                    return True

        # Draw
        if not self.get_moves():
            self.winner = None
            return True

        # Game not over yet
        else:
            return False

    def get_moves(self) -> list:
        """
        Returns a list of free (x, y) nodes.
        """

        def get_coordinates():
            for coords in np.argwhere(self._state == self.fill):
                yield tuple(coords)

        return list(get_coordinates())

    def get_random_move(self) -> tuple[int, int]:
        """
        Returns a random (x, y) available node.
        """
        moves = self.get_moves()
        return choice(moves)

    def move(self, x: int, y: int, player: int) -> None:
        """
        Updates the board with a new move at <(x, y)> from <player>.

        :param x: x coordinate
        :param y: y coordinate
        :param player: current player
        """
        self.state = x, y, player

    def undo(self, x: int, y: int) -> None:
        """
        Undo a move.

        :param x: x coordinate
        :param y: y coordinate
        """
        self.state = x, y, self.fill
