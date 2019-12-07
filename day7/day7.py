import itertools

from IntCoder import IntCoder, IntCoderWithIo

memory = IntCoder.read_file('./input.txt')


def run(seq):
    current = 0
    for phase in seq:
        coder = IntCoderWithIo(memory, [phase, current])
        coder.run()
        current = coder.output
    return current


_max = 0
c = itertools.permutations([0, 1, 2, 3, 4], 5)
for sequence in c:
    value = run(sequence)
    if value > _max:
        _max = value

print(_max)  # part 1
