import itertools

from IntCoder import IntCoder
from Day7Coder import Day7Coder

memory = IntCoder.read_file('./input.txt')


def run(seq):
    c1 = Day7Coder(memory, seq[0])
    c2 = Day7Coder(memory, seq[1])
    c3 = Day7Coder(memory, seq[2])
    c4 = Day7Coder(memory, seq[3])
    c5 = Day7Coder(memory, seq[4])
    while c5.read_pointer() != 99:
        c1.run()
        c2.run()
        c3.run()
        c4.run()
        c5.run()


_max = 0
for sequence in itertools.permutations([5, 6, 7, 8, 9], 5):
    Day7Coder.state = 0
    run(sequence)
    if Day7Coder.state > _max:
        _max = Day7Coder.state
print(_max)
