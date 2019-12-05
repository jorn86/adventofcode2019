def run(input_value):
    pointer = 0
    memory = [int(i) for i in open('./input.txt', 'r').read().split(',')]

    def step(address):
        instruction = memory[address]
        opcode = instruction % 100
        pm1 = (instruction // 100) % 10
        pm2 = (instruction // 1000) % 10
        # pm3 = instruction // 10000

        i1 = memory[address + 1]
        v1 = memory[i1] if pm1 == 0 else i1

        if opcode == 3:
            memory[i1] = input_value
            return address + 2
        if opcode == 4:
            print('output = {}'.format(v1))
            return address + 2

        i2 = memory[address + 2]
        v2 = memory[i2] if pm2 == 0 else i2

        if opcode == 5:
            return v2 if v1 != 0 else address + 3
        if opcode == 6:
            return v2 if v1 == 0 else address + 3

        i3 = memory[address + 3]
        if opcode == 1:
            memory[i3] = v1 + v2
        if opcode == 2:
            memory[i3] = v1 * v2
        if opcode == 7:
            memory[i3] = 1 if v1 < v2 else 0
        if opcode == 8:
            memory[i3] = 1 if v1 == v2 else 0
        return address + 4

    while memory[pointer] is not 99:
        pointer = step(pointer)

    return memory[0]


run(1)  # part 1
run(5)  # part 2
