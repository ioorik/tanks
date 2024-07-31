class Bullet:

    def __init__(self, x, y, direction):
        self.facing = direction
        self.y = y
        self.x = x
        self.acc = 0.01

    def update(self, walls):
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
                x - 0.5 + width > self.x > x - 0.5
                and y + height - 0.5 > self.y > y - 0.5
            ) or (
                x - 0.5 < self.x < x + width - 0.5
                and y + height - 0.5 > self.y > y - 0.5
            ):
                return False

        return True
