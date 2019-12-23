from collections import deque
from typing import List, Deque, Dict

from IntCoder import IntCoder


class Day23Coder(IntCoder):
    nat = (0, 0)

    def __init__(self, program: List[int], address, queues: Dict[int, Deque[int]]):
        super().__init__(IntCoder.extended_memory(program, 10000))
        self.address = address
        self.queues = queues
        self.out_cache = []
        self.first_input = True

    def get_input(self) -> int:
        if self.first_input:
            self.first_input = False
            print(f'init {self.address}')
            return self.address
        own_queue = self.queues[self.address]
        if len(own_queue) == 0:
            return -1
        return own_queue.popleft()

    def handle_output(self, value: int):
        self.out_cache.append(value)
        if len(self.out_cache) == 3:
            address = self.out_cache[0]
            x = self.out_cache[1]
            y = self.out_cache[2]
            if address == 255:
                print(f'to nat: ({x}, {y})')  # first print of this is part 1
                Day23Coder.nat = (x, y)
            else:
                target_queue = self.queues[address]
                target_queue.append(x)
                target_queue.append(y)
            self.out_cache = []

    def run(self) -> None:
        super().run()
        print(f'{self.address} finished')


io = {i: deque() for i in range(50)}
coders = [Day23Coder(IntCoder.read_file('./input.txt'), i, io) for i in range(50)]

while True:
    all_empty = True
    for coder in coders:
        coder._step()
        all_empty &= len(io[coder.address]) == 0
    if all_empty and Day23Coder.nat != (0, 0):
        print(f'sending nat {Day23Coder.nat}')  # last print of this is part 2
        io[0].append(Day23Coder.nat[0])
        io[0].append(Day23Coder.nat[1])
        Day23Coder.nat = (0, 0)
