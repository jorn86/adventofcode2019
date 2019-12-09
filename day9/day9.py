from IntCoder import IntCoder, IntCoderWithIo

memory = IntCoder.extended_memory(IntCoder.read_file('input.txt'), 1077)
coder = IntCoderWithIo(memory, [1])
coder.run()
print(coder.output)  # part 1

coder = IntCoderWithIo(memory, [2])
coder.run()
print(coder.output)  # part 2

