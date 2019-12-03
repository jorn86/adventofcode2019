def run(input1, input2):
    pointer = 0
    memory = [int(i) for i in open('./input.txt', 'r').read().split(',')]
    memory[1] = input1
    memory[2] = input2

    def step(address):
        opcode = memory[address]
        i1 = memory[address + 1]
        i2 = memory[address + 2]
        i3 = memory[address + 3]

        if opcode == 1:
            memory[i3] = memory[i1] + memory[i2]
        if opcode == 2:
            memory[i3] = memory[i1] * memory[i2]

    while memory[pointer] is not 99:
        step(pointer)
        pointer += 4

    return memory[0]


print(run(12, 2))  # part 1

for in1 in range(0, 99):
    for in2 in range(0, 99):
        if run(in1, in2) == 19690720:
            print('{}{}'.format(in1, in2))  # part 2
