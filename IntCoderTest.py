import unittest

from IntCoder import IntCoder, IntCoderWithIo


class IntCoderTest(unittest.TestCase):
    def test_invalid_input(self):
        with self.assertRaises(StopIteration):
            IntCoderWithIo([3, 1, 99], []).run()

    def test_day2_example1(self):
        coder = IntCoder([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50])
        coder.run()
        self.assertEqual([3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50], coder._memory)

    def test_day2_example2(self):
        coder = IntCoder([1, 0, 0, 0, 99])
        coder.run()
        self.assertEqual([2, 0, 0, 0, 99], coder._memory)

    def test_day2_example3(self):
        coder = IntCoder([2, 3, 0, 3, 99])
        coder.run()
        self.assertEqual([2, 3, 0, 6, 99], coder._memory)

    def test_day2_example4(self):
        coder = IntCoder([2, 4, 4, 5, 99, 0])
        coder.run()
        self.assertEqual([2, 4, 4, 5, 99, 9801], coder._memory)

    def test_day2_example5(self):
        coder = IntCoder([1, 1, 1, 4, 99, 5, 6, 0, 99])
        coder.run()
        self.assertEqual([30, 1, 1, 4, 2, 5, 6, 0, 99], coder._memory)

    def test_day2_part1(self):
        memory = IntCoder.read_file('./day2/input.txt')
        memory[1] = 12
        memory[2] = 2
        coder = IntCoder(memory)
        coder.run()
        self.assertEqual(2782414, coder.read(0))

    def test_day2_part2(self):
        memory = IntCoder.read_file('./day2/input.txt')
        memory[1] = 98
        memory[2] = 20
        coder = IntCoder(memory)
        coder.run()
        self.assertEqual(19690720, coder.read(0))

    def test_day5_example1(self):
        coder = IntCoder([1002, 4, 3, 4, 33])
        coder.run()
        self.assertEqual([1002, 4, 3, 4, 99], coder._memory)

    def test_day5_example2(self):
        coder = IntCoder([1101, 100, -1, 4, 0])
        coder.run()
        self.assertEqual([1101, 100, -1, 4, 99], coder._memory)

    def test_day5_example3(self):
        self.__day5([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], 7, 0)
        self.__day5([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], 8, 1)
        self.__day5([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], 9, 0)

        self.__day5([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8], 7, 1)
        self.__day5([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8], 8, 0)

        self.__day5([3, 3, 1108, -1, 8, 3, 4, 3, 99], 7, 0)
        self.__day5([3, 3, 1108, -1, 8, 3, 4, 3, 99], 8, 1)
        self.__day5([3, 3, 1108, -1, 8, 3, 4, 3, 99], 9, 0)

        self.__day5([3, 3, 1107, -1, 8, 3, 4, 3, 99], 7, 1)
        self.__day5([3, 3, 1107, -1, 8, 3, 4, 3, 99], 8, 0)

    def test_day5_example4(self):
        memory = [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31, 1106, 0, 36, 98, 0, 0, 1002, 21,
                  125, 20, 4, 20, 1105, 1, 46, 104, 999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99]
        self.__day5(memory, 7, 999)
        self.__day5(memory, 8, 1000)
        self.__day5(memory, 9, 1001)

    def test_day5_part1(self):
        self.__day5(IntCoder.read_file('./day5/input.txt'), 1, 3122865)

    def test_day5_part2(self):
        self.__day5(IntCoder.read_file('./day5/input.txt'), 5, 773660)

    def __day5(self, memory, input_value, output):
        self.assertEqual(output, self.__with_io(memory, [input_value])[-1])

    def test_day7_example1(self):
        self.__day7_part1([3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0], [4, 3, 2, 1, 0], 43210)
        self.__day7_part1(
            [3, 23, 3, 24, 1002, 24, 10, 24, 1002, 23, -1, 23, 101, 5, 23, 23, 1, 24, 23, 23, 4, 23, 99, 0, 0],
            [0, 1, 2, 3, 4], 54321)
        self.__day7_part1(
            [3, 31, 3, 32, 1002, 32, 10, 32, 1001, 31, -2, 31, 1007, 31, 0, 33, 1002, 33, 7, 33, 1, 33, 31, 31,
             1, 32, 31, 31, 4, 31, 99, 0, 0, 0], [1, 0, 4, 3, 2], 65210)

    def test_day7_part1(self):
        self.__day7_part1(IntCoder.read_file('./day7/input.txt'), [3, 1, 4, 2, 0], 92663)

    def __day7_part1(self, memory, sequence, answer):
        v1 = self.__with_io(memory, [sequence[0], 0])[-1]
        v2 = self.__with_io(memory, [sequence[1], v1])[-1]
        v3 = self.__with_io(memory, [sequence[2], v2])[-1]
        v4 = self.__with_io(memory, [sequence[3], v3])[-1]
        v5 = self.__with_io(memory, [sequence[4], v4])[-1]
        self.assertEqual(answer, v5)

    def test_day9_example(self):
        program = [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]
        self.__day9(IntCoder.extended_memory(program, 102), [], program)
        self.__day9([1102, 34915192, 34915192, 7, 4, 7, 99, 0], [], [1219070632396864])
        self.__day9([104, 1125899906842624, 99], [], [1125899906842624])

    def test_day9_part1(self):
        self.__day9(IntCoder.extended_memory(IntCoder.read_file('./day9/input.txt'), 1030), [1], [3839402290])

    def test_day9_part2(self):
        self.__day9(IntCoder.extended_memory(IntCoder.read_file('./day9/input.txt'), 1077), [2], [35734])

    def __day9(self, memory, _in, output):
        self.assertEqual(output, self.__with_io(memory, _in))

    @staticmethod
    def __with_io(memory, input_values):
        coder = IntCoderWithIo(memory, input_values)
        coder.run()
        return coder.output
