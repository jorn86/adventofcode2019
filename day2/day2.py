from IntCoder import IntCoder


def run(input1, input2):
    memory = [int(i) for i in open('./input.txt', 'r').read().split(',')]
    memory[1] = input1
    memory[2] = input2
    IntCoder(memory).run()
    return memory[0]


print(run(12, 2))  # part 1

for in1 in range(0, 99):
    for in2 in range(0, 99):
        if run(in1, in2) == 19690720:
            print(f'{in1}{in2}')  # part 2
