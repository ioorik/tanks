import pygame
from tanks.TanksTypes.Player import Player
from tanks.Bullet import Bullet


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
        self.wallTexture = pygame.image.load("tanks/Assets/wall.png")

        self.bullets: list[Bullet] = []

        self.win = pygame.display.set_mode((width, height), pygame.RESIZABLE)

        self.player = Player(0, 0)
        self.walls = [[2, 0, 2, 1]]

    def run(self):
        bulletCooldown = 0
        while True:
            self.win.fill(self.bg)

            self.width = self.win.get_width()
            self.height = self.win.get_height()

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    return False

            keys = pygame.key.get_pressed()

            self.player.update(keys, self.walls, self.gs)

            if keys[pygame.K_SPACE] and bulletCooldown <= 0:
                self.bullets.append(
                    Bullet(self.player.x(), self.player.y(), self.player.facing())
                )
                bulletCooldown = 1000

            pImg = pygame.transform.rotate(self.tank1, self.player.facing() * 90)
            pImg = pygame.transform.scale(pImg, (self.gs, self.gs))
            self.win.blit(
                pImg,
                (
                    self.width / 2 + self.player.x() * self.gs - self.gs / 2,
                    self.height / 2 - self.player.y() * self.gs - self.gs / 2,
                ),
            )

            wImg = pygame.transform.scale(self.wallTexture, (self.gs, self.gs))
            for wall in self.walls:
                x, y, width, height = wall
                for i in range(width):
                    for j in range(height):
                        self.win.blit(
                            wImg,
                            (
                                self.width / 2
                                + x * self.gs
                                + i * self.gs
                                - self.gs / 2,
                                self.height / 2
                                - y * self.gs
                                + j * self.gs
                                - self.gs / 2,
                            ),
                        )

            for j in range(len(self.bullets)):
                bullet = self.bullets[j]
                for i in range(len(self.bullets)):
                    if (
                        bullet.x > self.width / 2
                        or bullet.x < -self.width / 2
                        or bullet.y > self.height / 2
                        or bullet.y < -self.height / 2
                    ):
                        self.bullets.pop(i)
                        break
                if bullet.update(self.walls):
                    pygame.draw.rect(
                        self.win,
                        (255, 255, 255),
                        (
                            self.width / 2 + bullet.x * self.gs - self.gs / 4 / 2,
                            self.height / 2 - bullet.y * self.gs - self.gs / 4 / 2,
                            self.gs / 4,
                            self.gs / 4,
                        ),
                    )
                else:
                    self.bullets.pop(j)
                    break

            pygame.display.flip()

            bulletCooldown -= 1


if __name__ == "__main__":
    win = Window(800, 600, 50, (255, 255, 255), (0, 0, 0))
    win.run()
