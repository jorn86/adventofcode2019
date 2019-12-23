from IntCoder import IntCoder

program = \
    'NOT C J\n' \
    'NOT B T\n' \
    'OR T J\n' \
    'NOT A T\n' \
    'OR T J\n' \
    'AND D J\n' \
    'WALK\n'
coder = IntCoder(IntCoder.extended_memory(IntCoder.read_file('./input.txt'), 10000), [ord(c) for c in program])
coder.run()
if len(coder.output) != 34:
    print(''.join([chr(n) for n in coder.output[:-1]]))  # error
else:
    print(coder.output[-1])  # answer
