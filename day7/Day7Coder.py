from typing import List

from IntCoder import IntCoder


class Day7Coder(IntCoder):
    state = 0

    def __init__(self, mem: List[int], first_input: int):
        super(Day7Coder, self).__init__(mem)
        self.first_input = first_input
        self.first = True

    def get_input(self):
        if self.first:
            self.first = False
            return self.first_input
        return Day7Coder.state

    def handle_output(self, value):
        Day7Coder.state = value
        return False

