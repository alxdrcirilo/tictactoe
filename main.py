from tictactoe.board import Board


if __name__ == "__main__":
    board = Board()

    while not board.is_game_over():
        x, y = board.get_random_move()
        board.move(x=x, y=y, player=board.player)
        board.next_player()

    over, winner = board.is_game_over()
    print(f"{winner=}")
    print(f"{board}")
