from IntCoder import IntCoder

memory = IntCoder.extended_memory(IntCoder.read_file('input.txt'), 1077)
coder = IntCoder(memory, [1])
coder.run()
print(coder.output)  # part 1

coder = IntCoder(memory, [2])
coder.run()
print(coder.output)  # part 2

