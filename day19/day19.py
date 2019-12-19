from IntCoder import IntCoder

result = 0
program = IntCoder.read_file('./input.txt')
for x in range(50):
    for y in range(50):
        coder = IntCoder(IntCoder.extended_memory(program, 10000), [x, y])
        coder.run()
        result += coder.output[0]
print(result)
