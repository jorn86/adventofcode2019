from typing import List, Iterable


class IntCoder:
    def __init__(self, memory: List[int], input_values: Iterable[int] = None):
        self._memory = memory
        self._pointer = 0
        self._relative_base = 0
        self._input = iter(input_values or [])
        self.output = []
        self._opcodes = {
            1: self._add,
            2: self._multiply,
            3: self._in,
            4: self._out,
            5: self._if_true,
            6: self._if_false,
            7: self._less_than,
            8: self._equal,
            9: self._adjust_relative_base,
            99: self._halt,
        }

    def run(self) -> None:
        while self._step():
            pass

    def get_input(self) -> int:
        try:
            return next(self._input)
        except StopIteration:
            raise ValueError('Input exhausted')

    def handle_output(self, value: int):
        self.output.append(value)
        return True

    def peek_pointer(self) -> int:
        return self.peek_index(self._pointer)

    def peek_index(self, index: int) -> int:
        return self._memory[index]

    def _fetch(self):
        index = self._memory[self._pointer]
        self._pointer += 1
        return index

    def _index(self, mode):
        index = self._fetch()
        if mode == 0:
            return index
        elif mode == 2:
            return index + self._relative_base
        raise ValueError(f'Got mode {mode} for index only type param')

    def _val(self, mode):
        index = self._fetch()
        if mode == 0:
            return self._memory[index]
        elif mode == 1:
            return index
        elif mode == 2:
            return self._memory[index + self._relative_base]
        else:
            raise ValueError(f'Unknown parameter mode {mode}')

    def _step(self):
        instruction = self._fetch()
        opcode = instruction % 100
        mode1 = (instruction // 100) % 10
        mode2 = (instruction // 1000) % 10
        mode3 = instruction // 10000
        try:
            return self._opcodes[opcode](mode1, mode2, mode3)
        except KeyError:
            raise ValueError(f'Unknown opcode {opcode} in instruction {instruction}')

    def _add(self, mode1, mode2, mode3):
        first = self._val(mode1)
        second = self._val(mode2)
        self._memory[self._index(mode3)] = first + second
        return True

    def _multiply(self, mode1, mode2, mode3):
        first = self._val(mode1)
        second = self._val(mode2)
        self._memory[self._index(mode3)] = first * second
        return True

    def _in(self, mode1, mode2, mode3):
        self._memory[self._index(mode1)] = self.get_input()
        return True

    def _out(self, mode1, mode2, mode3):
        return self.handle_output(self._val(mode1))

    def _if_true(self, mode1, mode2, mode3):
        #  do not inline, values always need to be read in order to increment pointer
        first = self._val(mode1)
        second = self._val(mode2)
        if first != 0:
            self._pointer = second
        return True

    def _if_false(self, mode1, mode2, mode3):
        #  do not inline, values always need to be read in order to increment pointer
        first = self._val(mode1)
        second = self._val(mode2)
        if first == 0:
            self._pointer = second
        return True

    def _less_than(self, mode1, mode2, mode3):
        first = self._val(mode1)
        second = self._val(mode2)
        self._memory[self._index(mode3)] = 1 if first < second else 0
        return True

    def _equal(self, mode1, mode2, mode3):
        first = self._val(mode1)
        second = self._val(mode2)
        self._memory[self._index(mode3)] = 1 if first == second else 0
        return True

    def _adjust_relative_base(self, mode1, mode2, mode3):
        self._relative_base += self._val(mode1)
        return True

    @staticmethod
    def _halt(mode1, mode2, mode3):
        return False

    @staticmethod
    def extended_memory(program: List[int], size: int):
        memory = [0] * size
        memory[0:len(program)] = program
        return memory

    @staticmethod
    def read_file(file: str):
        with open(file, 'r') as f:
            return [int(s) for s in f.read().split(',')]

