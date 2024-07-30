import pygame
from tanks.TanksTypes.Player import Player


class Window:

    def __init__(self, width, height, defColor, bgColor):
        self.width = width
        self.height = height
        self.color = defColor
        self.bg = bgColor

        self.tank1 = pygame.image.load("Assets/tank1.png")

        self.win = pygame.display.set_mode((width, height), pygame.RESIZABLE)

    def frame(self, player: Player, gs: float):
        self.win.fill(self.bg)

        self.width = self.win.get_width()
        self.height = self.win.get_height()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return False

        newImg = pygame.transform.rotate(self.tank1, player.facing() * 90)
        self.win.blit(
            newImg, (self.width / 2 + player.x(), self.height / 2 - player.y())
        )

        # pygame.draw.rect(
        #     self.win,
        #     self.color,
        #     (
        #         self.width / 2 + player.x() - gs / 2,
        #         self.height / 2 - player.y() - gs / 2,
        #         gs,
        #         gs,
        #     ),
        # )

        pygame.display.flip()

        return pygame.key.get_pressed()


if __name__ == "__main__":
    win = Window(800, 600, (255, 255, 255), (0, 0, 0))
