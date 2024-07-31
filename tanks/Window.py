import pygame
from tanks.TanksTypes.Player import Player
from tanks.TanksTypes.Tank1 import Tank1
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

        self.playerImg = pygame.image.load("tanks/Assets/player.png")
        self.wallImg = pygame.image.load("tanks/Assets/wall.png")
        self.enemyImg1 = pygame.image.load("tanks/Assets/tank1.png")

        pixels = pygame.PixelArray(self.wallImg)
        # Iterate over every pixel
        for x in range(self.wallImg.get_width()):
            for y in range(self.wallImg.get_height()):
                # Turn the pixel data into an RGB tuple
                rgb = self.wallImg.unmap_rgb(pixels[x][y])
                # Get a new color object using the RGB tuple and convert to HSLA
                color = pygame.Color(*rgb)
                h, s, l, a = color.hsla
                # Add 120 to the hue (or however much you want) and wrap to under 360
                color.hsla = (int(h) + 220) % 360, int(s), int(l), int(a)
                # Assign directly to the pixel
                pixels[x][y] = color

        self.bullets: list[Bullet] = []

        self.win = pygame.display.set_mode((width, height), pygame.RESIZABLE)

        self.player = Player(0, 0)
        self.enemies: list[Tank1] = []
        self.walls = [
            [
                -width // gridSize // 2 - 0.5,
                height // gridSize // 2 - 0.5,
                width // gridSize + 1,
                1,
            ],
            [
                -width // gridSize // 2 + 0.5,
                height // gridSize // 2 - 1.5,
                1,
                height // gridSize - 2,
            ],
            [
                -width // gridSize // 2 - 0.5,
                -height // gridSize // 2 + 0.5,
                width // gridSize + 1,
                1,
            ],
            [
                0,
                0,
                1,
                1,
            ],
        ]

    def run(self):
        bulletCooldown = 0
        enemyCool = 10000
        while True:
            if enemyCool <= 0:
                self.enemies.append(Tank1(0, 0))
                enemyCool = 10000
            self.win.fill(self.bg)

            self.width = self.win.get_width()
            self.height = self.win.get_height()

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    return False

            keys = pygame.key.get_pressed()

            self.player.update(keys, self.walls)

            for enemy in self.enemies:
                if enemy.update(keys, self.walls):
                    self.bullets.append(Bullet(enemy.x(), enemy.y(), enemy.facing()))

            if keys[pygame.K_SPACE] and bulletCooldown <= 0:
                self.bullets.append(
                    Bullet(self.player.x(), self.player.y(), self.player.facing())
                )
                bulletCooldown = 1000

            pImg = pygame.transform.rotate(self.playerImg, self.player.facing() * 90)
            newPImg = pygame.Surface((self.gs, self.gs))
            pygame.transform.scale(pImg, (self.gs, self.gs), newPImg)
            self.win.blit(
                newPImg,
                (
                    self.width / 2 + self.player.x() * self.gs - self.gs / 2,
                    self.height / 2 - self.player.y() * self.gs - self.gs / 2,
                ),
            )

            for enemy in self.enemies:
                eImg = pygame.transform.rotate(self.enemyImg1, enemy.facing() * 90)
                newEImg = pygame.Surface((self.gs, self.gs))
                eImg = pygame.transform.scale(eImg, (self.gs, self.gs), newEImg)
                self.win.blit(
                    eImg,
                    (
                        self.width / 2 + enemy.x() * self.gs - self.gs / 2,
                        self.height / 2 - enemy.y() * self.gs - self.gs / 2,
                    ),
                )

            newWImg = pygame.Surface((self.gs, self.gs))
            wImg = pygame.transform.scale(self.wallImg, (self.gs, self.gs), newWImg)
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
                if bullet.update(self.walls, self.bullets, self.player, self.enemies):
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
            enemyCool -= 1


if __name__ == "__main__":
    win = Window(800, 600, 50, (255, 255, 255), (0, 0, 0))
    win.run()
