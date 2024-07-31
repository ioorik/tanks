import numpy as np


class Bullet:

    def __init__(self, x, y, direction, isEnemy):
        self.facing = direction
        self.time = 10
        self.y = y
        self.x = x
        self.acc = 0.004
        self.isEnemy = isEnemy

        if self.facing == 0:
            self.y += 0.5
        elif self.facing == 1:
            self.x -= 0.5
        elif self.facing == 2:
            self.y -= 0.5
        elif self.facing == 3:
            self.x += 0.5

    def update(self, walls, bullets, player, enemies):
        self.time -= 1
        if self.facing == 0:
            self.y += self.acc
        elif self.facing == 1:
            self.x -= self.acc
        elif self.facing == 2:
            self.y -= self.acc
        elif self.facing == 3:
            self.x += self.acc

        for wall in walls:
            x, y, width, height = wall
            if (
                x + width - 0.5 > self.x > x - 0.5
                and y + 0.5 > self.y > y - height + 0.5
            ):
                return [False, None, False, None]

        for i in range(len(bullets)):
            bullet = bullets[i]
            if bullet != self:
                dst = np.sqrt((bullet.x - self.x) ** 2 + (bullet.y - self.y) ** 2)
                if dst < 0.2:
                    return [False, i, False, None]

        if self.time < 0:
            dst = np.sqrt((player.x() - self.x) ** 2 + (player.y() - self.y) ** 2)
            if dst < 0.5:
                return [False, None, True, None]

        if not self.isEnemy:
            for i in range(len(enemies)):
                enemy = enemies[i]
                dst = np.sqrt((enemy.x() - self.x) ** 2 + (enemy.y() - self.y) ** 2)
                if dst < 0.5:
                    return [False, None, False, i]

        return [True, None, False, None]
