import logging
import time
from math import inf

import pandas as pd

from tictactoe.play import Play

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class Tournament:
    def __init__(self, sizes: range, depths: range, n: range) -> None:
        assert sizes.start >= 3, "Minimum board size is 3"
        assert depths.start >= 1, "Minimum depth is 1"
        assert n.start >= 0, "Minimum number of replicates is 1"
        self.modes = [
            "random_vs_random",
            "random_vs_minimax",
            "random_vs_minimax_ab",
        ]
        self.games = range(100)
        self.sizes = sizes
        self.depths = depths
        self.n = n

    def play(self) -> None:
        def run():
            start = time.process_time()

            winners = {0: 0, 1: 0, None: 0}
            for i in self.games:
                game = Play(size=s)
                if m == "random_vs_random":
                    game.random()
                elif m == "random_vs_minimax":
                    game.minimax(depth=d)
                elif m == "random_vs_minimax_ab":
                    game.minimax(depth=d, alpha=-inf, beta=inf)
                winners[game.board.winner] += 1

            elapsed = time.process_time() - start

            outcomes = {1: "win", 0: "loss", None: "draw"}
            for k, v in outcomes.items():
                data.append([m, s, d, v, winners[k], elapsed])

            logging.info(f"{m=} {s=} {d=}-{n}\t{round(elapsed, 2)}s")

        data = []
        for m in self.modes:
            for s in self.sizes:
                for d in self.depths:
                    for n in self.n:
                        run()

        header = ["mode", "size", "depth", "result", "value", "runtime"]
        stats = pd.DataFrame(data, columns=header)
        stats.to_csv(path_or_buf="tournament.csv", index=False)
