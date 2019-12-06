import unittest

from IntCoder import IntCoder, IntCoderWithIo


class IntCoderTest(unittest.TestCase):
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
        self.__day5_example([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], 7, 0)
        self.__day5_example([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], 8, 1)
        self.__day5_example([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], 9, 0)

        self.__day5_example([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8], 7, 1)
        self.__day5_example([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8], 8, 0)

        self.__day5_example([3, 3, 1108, -1, 8, 3, 4, 3, 99], 7, 0)
        self.__day5_example([3, 3, 1108, -1, 8, 3, 4, 3, 99], 8, 1)
        self.__day5_example([3, 3, 1108, -1, 8, 3, 4, 3, 99], 9, 0)

        self.__day5_example([3, 3, 1107, -1, 8, 3, 4, 3, 99], 7, 1)
        self.__day5_example([3, 3, 1107, -1, 8, 3, 4, 3, 99], 8, 0)

    def test_day5_example4(self):
        memory = [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31, 1106, 0, 36, 98, 0, 0, 1002, 21,
                  125, 20, 4, 20, 1105, 1, 46, 104, 999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99]
        self.__day5_example(memory, 7, 999)
        self.__day5_example(memory, 8, 1000)
        self.__day5_example(memory, 9, 1001)

    def __day5_example(self, memory, input_value, output):
        self.assertEqual(self.__with_io(memory, input_value), output)

    def test_day5_part1(self):
        out = self.__with_io(IntCoder.read_file('./day5/input.txt'), 1)
        self.assertEqual(3122865, out)

    def test_day5_part2(self):
        out = self.__with_io(IntCoder.read_file('./day5/input.txt'), 5)
        self.assertEqual(773660, out)

    @staticmethod
    def __with_io(memory, input_value):
        coder = IntCoderWithIo(memory, input_value)
        coder.run()
        return coder.output
