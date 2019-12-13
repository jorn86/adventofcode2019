from IntCoder import IntCoder

coder = IntCoder(IntCoder.extended_memory(IntCoder.read_file('input.txt'), 2659))
coder.run()
outputs = [coder.output[i:i+3] for i in range(0, len(coder.output), 3)]

count = 0
for o in outputs:
    if o[2] == 2:
        count += 1

print(count)
