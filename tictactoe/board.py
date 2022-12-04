import numpy as np
from random import choice


class Board():
    """
    Tic-tac-toe board class.
    Contains the state of the board and basic methods.
    """

    def __init__(self, starter: int = 0, fill: int = 2) -> None:
        """
        Initializes the board.

        :param starter: starting player (default: 0)
        :param fill: board state empty value (default: 2)
        """
        self.fill = fill
        self.mapping = {0: "O", 1: "X", 2: " "}

        self._state = np.full(shape=(3, 3),
                              fill_value=self.fill,
                              dtype=np.int8)
        self._player = starter

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

    def next_player(self) -> None:
        """
        Sets the next player.
        """
        players = [0, 1]
        players.remove(self.player)
        self.player = players[0]

    def get_hash(self) -> int:
        """
        Returns the hash value of a given board state.
        """
        return hash(str(self._state))

    def is_game_over(self) -> bool | tuple[bool, int]:
        """
        Checks if the game is over for both players:
        row-wise, column-wise, and on each diagonal.
        Also checks if the game reaches a draw.
        """
        if self.get_available_moves():
            # Check both players
            for player in [0, 1]:
                # Check diagonal
                if np.all(self._state.diagonal() == player):
                    return True, player
                # Check row-wise (0) and column-wise(1)
                for ax in [0, 1]:
                    if np.all(self._state == player, axis=ax).any():
                        return True, player
            # Game not over
            return False
        else:
            # Draw
            return True, 2

    def get_available_moves(self) -> list:
        """
        Returns a list of free (x, y) nodes.
        """
        return [tuple(coords) for coords in np.argwhere(self._state == self.fill)]

    def get_random_move(self) -> tuple[int, int]:
        """
        Returns a random (x, y) available node.
        """
        moves = self.get_available_moves()
        return choice(moves)

    def move(self, x: int, y: int, player: int) -> None:
        """
        Updates the board with a new move at <(x, y)> from <player>.

        :param x: x coordinate
        :param y: y coordinate
        :param player: current player
        """
        self.state = x, y, player
