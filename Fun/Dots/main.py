import pygame

colorTable = {"water": (0, 0, 255), "sand": (255, 0, 0), "air": (0, 255, 0)}


def pixel(surface, color, pos):
    pygame.draw.circle(surface, color, pos, 1)


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
                self.array[row][col] = Dot("water")

    def add(self, pos, type):
        self.array[pos] = Dot(type)


# def DrawDots(surface, map, table):
#     for i, item in enumerate(map.array):
#         for j in range(len(item)):
#             color = table.get(j.type)
#             pixel(surface, color, (i, j))
def DrawDots(surface, map, table):
    x = 0
    y = 0
    for i in map.array:
        y = y + 1
        x = 0
        for j in i:
            x = x + 1
            color = table.get(j.type)
            pixel(surface, color, (y, x))


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
                print("mouseup")
                # pos = pygame.mouse.get_pos()
                # dotMap.add(pos, "sand")
                DrawDots(screen, dotMap, colorTable)
                pixel(screen, (255, 55, 55), (10, 10))


if __name__ == "__main__":
    main()
