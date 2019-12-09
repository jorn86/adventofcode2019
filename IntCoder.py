import threading
from typing import List


class IntCoder:
    _memory = []
    __pointer = 0

    def __init__(self, memory: List[int]):
        self._memory = memory

    def run(self):
        while self.__step():
            pass

    def get_input(self):
        raise ValueError('No input defined')

    def handle_output(self, value):
        print(value)

    def read_pointer(self):
        return self.read(self.__pointer)

    def read(self, index):
        return self._memory[index]

    def __step(self):
        instruction = self._memory[self.__pointer]
        opcode = instruction % 100
        mode1 = (instruction // 100) % 10
        mode2 = (instruction // 1000) % 10
        mode3 = instruction // 10000
        if opcode == 1:
            self.__add(self.__val(self.__pointer + 1, mode1), self.__val(self.__pointer + 2, mode2), self.__index(self.__pointer + 3, mode3))
        elif opcode == 2:
            self.__mul(self.__val(self.__pointer + 1, mode1), self.__val(self.__pointer + 2, mode2), self.__index(self.__pointer + 3, mode3))
        elif opcode == 3:
            self.__in(self.__index(self.__pointer + 1, mode1))
        elif opcode == 4:
            self.__out(self.__val(self.__pointer + 1, mode1))
            return False
        elif opcode == 5:
            self.__if_true(self.__val(self.__pointer + 1, mode1), self.__val(self.__pointer + 2, mode2))
        elif opcode == 6:
            self.__if_false(self.__val(self.__pointer + 1, mode1), self.__val(self.__pointer + 2, mode2))
        elif opcode == 7:
            self.__lt(self.__val(self.__pointer + 1, mode1), self.__val(self.__pointer + 2, mode2), self.__index(self.__pointer + 3, mode3))
        elif opcode == 8:
            self.__eq(self.__val(self.__pointer + 1, mode1), self.__val(self.__pointer + 2, mode2), self.__index(self.__pointer + 3, mode3))
        elif opcode == 99:
            return False
        else:
            raise ValueError('Unknown opcode {} in instruction {}'.format(opcode, instruction))
        return True

    def __val(self, address, mode):
        index = self._memory[address]
        if mode == 0:
            return self._memory[index]
        elif mode == 1:
            return index
        else:
            raise ValueError('Unknown parameter mode {}'.format(mode))

    def __index(self, address, mode):
        if mode != 0:
            raise ValueError('Got mode {} for index only type param'.format(mode))
        return self._memory[address]

    def __add(self, first, second, result):
        self._memory[result] = first + second
        self.__pointer += 4

    def __mul(self, first, second, result):
        self._memory[result] = first * second
        self.__pointer += 4

    def __in(self, index):
        self._memory[index] = self.get_input()
        self.__pointer += 2

    def __out(self, value):
        self.handle_output(value)
        self.__pointer += 2

    def __if_true(self, first, second):
        self.__pointer = second if first != 0 else self.__pointer + 3

    def __if_false(self, first, second):
        self.__pointer = second if first == 0 else self.__pointer + 3

    def __lt(self, first, second, result):
        self._memory[result] = 1 if first < second else 0
        self.__pointer += 4

    def __eq(self, first, second, result):
        self._memory[result] = 1 if first == second else 0
        self.__pointer += 4

    @staticmethod
    def read_file(file):
        with open(file, 'r') as f:
            return [int(s) for s in f.read().split(',')]


class IntCoderWithIo(IntCoder):
    def __init__(self, memory, input_values: List[int]):
        super(IntCoderWithIo, self).__init__(memory)
        self.input_values = (n for n in input_values)
        self.output = None

    def get_input(self):
        return next(self.input_values)

    def handle_output(self, value):
        self.output = value
