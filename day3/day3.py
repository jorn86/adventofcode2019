def path_right(position, length):
    return [(position[0], i) for i in range(position[1] + 1, position[1] + length)]


def path_left(position, length):
    return [(position[0], i) for i in range(position[1] - 1, position[1] - length, -1)]


def path_up(position, length):
    return [(i, position[1]) for i in range(position[0] + 1, position[0] + length)]


def path_down(position, length):
    return [(i, position[1]) for i in range(position[0] - 1, position[0] - length, -1)]


def traverse(r, position, full_path):
    options = {
        'R': path_right,
        'L': path_left,
        'U': path_up,
        'D': path_down,
    }
    direction = r[0:1]
    length = int(r[1:]) + 1
    path_segment = options[direction](position, length)
    full_path.extend(path_segment)
    return path_segment[-1]


def path(route):
    full_path = [(0, 0)]
    position = (0, 0)
    for r in route:
        position = traverse(r, position, full_path)
    return full_path


file = open('input.txt').readlines()
first = file[0].split(',')
second = file[1].split(',')
first_path = path(first)
second_path = path(second)
crosses = set(first_path).intersection(set(second_path))
crosses.discard((0, 0))

print(min([abs(x[0]) + abs(x[1]) for x in crosses]))  # part 1

min_steps = 999999
for c in crosses:
    steps = first_path.index(c) + second_path.index(c)
    if min_steps > steps:
        min_steps = steps
print(min_steps)  # part 2
