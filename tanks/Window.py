import pygame
from tanks.TanksTypes.Player import Player


class Window:

    def __init__(
        self, width, height, gridSize, defColor=(255, 255, 255), bgColor=(0, 0, 0)
    ):
        self.width = width
        self.height = height
        self.color = defColor
        self.bg = bgColor
        self.gs = gridSize

        self.tank1 = pygame.image.load("tanks/Assets/tank1.png")

        self.win = pygame.display.set_mode((width, height), pygame.RESIZABLE)

        self.player = Player(0, 0)
        self.walls = [[2, 0, 1, 1]]

    def run(self):
        while True:
            self.win.fill(self.bg)
            self.player.update(pygame.key.get_pressed(), self.walls, self.gs)

            self.width = self.win.get_width()
            self.height = self.win.get_height()

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    return False

            newImg = pygame.transform.rotate(self.tank1, self.player.facing() * 90)
            newImg = pygame.transform.scale(newImg, (self.gs, self.gs))
            self.win.blit(
                newImg,
                (
                    self.width / 2 + self.player.x() * self.gs - self.gs / 2,
                    self.height / 2 - self.player.y() * self.gs - self.gs / 2,
                ),
            )

            for wall in self.walls:
                x, y, width, height = wall
                pygame.draw.rect(
                    self.win,
                    self.color,
                    (
                        self.width / 2 + x * self.gs - self.gs / 2,
                        self.height / 2 - y * self.gs - self.gs / 2,
                        self.gs * width,
                        self.gs * height,
                    ),
                )

            pygame.display.flip()


if __name__ == "__main__":
    win = Window(800, 600, 50, (255, 255, 255), (0, 0, 0))
    win.run()
