size = 25 * 6

with open('./input.txt', 'r') as f:
    inputs = [int(d) for d in f.read()]

layers = [inputs[i:i + size] for i in range(0, len(inputs), size)]

_min = 999
for layer in layers:
    zeroes = layer.count(0)
    if zeroes < _min:
        _min = zeroes
        ones = layer.count(1)
        twos = layer.count(2)
        print(f'{zeroes}: {ones}x{twos}={ones * twos}')


def paint(index):
    for layer in layers:
        if layer[index] != 2:
            return layer[index]


chars = ['\u2588' if paint(i) == 1 else ' ' for i in range(0, 150)]
for line in [''.join(chars[i:i + 25]) for i in range(0, 150, 25)]:
    print(line)
