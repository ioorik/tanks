from tanks.TanksTypes.Player import Player
from tanks.Window import Window


class main:

    def __init__(self):
        self.win = Window(800, 600, (255, 255, 255), (0, 0, 0))

        self.p = Player(0, 0)

        self.gridSize = 50

    def run(self):
        while True:
            keys = self.win.frame(self.p, self.gridSize)
            if not keys:
                return
            self.p.update(keys, [1, 0, 1, 1])


if __name__ == "__main__":
    main().run()
