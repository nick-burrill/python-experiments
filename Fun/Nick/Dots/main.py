import pygame

colorTable = {"water": (0, 0, 255), "sand": (255, 0, 0), "air": (0, 255, 0)}


def pixel(surface, color, pos):
    pygame.draw.circle(surface, color, pos, 0)


class Dot:
    def __init__(self, type):
        self.type = type


class DotMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.array = [[0] * width] * height

        for row in range(self.height):
            for col in range(self.width):
                # print((row, col))
                self.array[row][col] = Dot("air")

    def add(self, pos, type):
        self.array[pos] = Dot(type)


def DrawDots(surface, map, table):
    for i, item in enumerate(map.array):
        for j in range(len(item)):
            color = table.get(j.type)
            pixel(surface, color, (i, j))


def main():
    pygame.init()
    screenWidth = 240
    screenHeight = 180

    dotMap = DotMap(screenWidth, screenHeight)

    pygame.display.set_caption("Minimal Program")

    screen = pygame.display.set_mode((240, 180))

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                # pos = pygame.mouse.get_pos()
                # dotMap.add(pos, "sand")
                DrawDots(screen, dotMap, colorTable)


if __name__ == "__main__":
    main()