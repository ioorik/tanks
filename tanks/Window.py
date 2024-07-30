import pygame


class Window:

    def __init__(self, width, height, defColor, bgColor):
        self.width = width
        self.height = height
        self.color = defColor
        self.bg = bgColor

        self.win = pygame.display.set_mode((width, height), pygame.RESIZABLE)

        self._run()

    def _run(self):
        running = True
        while running:
            self.win.fill(self.bg)

            self.width = self.win.get_width()
            self.height = self.win.get_height()

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    running = False

            pygame.display.flip()


if __name__ == "__main__":
    win = Window(800, 600, (255, 255, 255), (0, 0, 0))
