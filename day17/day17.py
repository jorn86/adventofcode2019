from IntCoder import IntCoder

coder = IntCoder(IntCoder.extended_memory(IntCoder.read_file('./input.txt'), 4000))
coder.run()
width = coder.output.index(10) + 1
lines = [coder.output[i:i + width] for i in range(0, len(coder.output), width)]


def is_intersection(x, y):
    return lines[x][y] == 35 and lines[x-1][y] == 35 and lines[x+1][y] == 35 and lines[x][y-1] == 35 and lines[x][y+1] == 35


result = 0
for x in range(1, len(lines) - 2):
    for y in range(1, len(lines[x]) - 1):
        if is_intersection(x, y):
            result += (x * y)
print(result)
