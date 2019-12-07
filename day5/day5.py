from IntCoder import IntCoderWithIo


def run(input_value):
    memory = [int(i) for i in open('./input.txt', 'r').read().split(',')]
    coder = IntCoderWithIo(memory, [input_value])
    coder.run()
    print(coder.output)


run(1)  # part 1
run(5)  # part 2
