from typing import List

from IntCoder import IntCoder


class Ship:
    def __init__(self, height, width) -> None:
        super().__init__()
        self.moves = {
            0: (1, 0),   # up
            1: (0, -1),   # left
            2: (-1, 0),  # down
            3: (0, 1),  # right
        }
        self.grid = list([0] * height for _ in range(width))
        self.direction = 0
        self.position = (width // 2, height // 2)

    def read(self):
        return self.grid[self.position[0]][self.position[1]]

    def paint(self, color):
        self.grid[self.position[0]][self.position[1]] = color

    def turn(self, relative_direction):
        self.direction += relative_direction + 4
        self.direction %= 4

        move = self.moves[self.direction]
        self.position = (self.position[0] + move[0], self.position[1] + move[1])


class Day11Coder(IntCoder):
    def __init__(self, memory: List[int], ship):
        super().__init__(memory)
        self._next_is_color = True
        self.ship = ship

    def get_input(self) -> int:
        return self.ship.read()

    def handle_output(self, value: int):
        if self._next_is_color:
            self._next_is_color = False
            self.ship.paint(value)
            return True
        else:
            self._next_is_color = True
            self.ship.turn(1 if value == 1 else -1)
            return False

    @staticmethod
    def _halt(mode1, mode2, mode3):
        raise RuntimeError('finished')


def step(coder):
    try:
        coder.run()
        return True
    except RuntimeError:
        return False


def part1():
    ship = Ship(100, 100)
    coder = Day11Coder(IntCoder.extended_memory(IntCoder.read_file('./input.txt'), 1107), ship)
    covered = set()
    while step(coder):
        covered.add(ship.position)

    print(len(covered))


def part2():
    ship = Ship(80, 10)
    ship.paint(1)
    coder = Day11Coder(IntCoder.extended_memory(IntCoder.read_file('./input.txt'), 851), ship)
    while step(coder):
        pass
    ship.grid.reverse()
    for line in ship.grid:
        chars = ['\u2588' if c == 1 else ' ' for c in line]
        chars.reverse()
        print(''.join(chars))


part1()
part2()
