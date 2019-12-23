class Deck:
    def __init__(self, size) -> None:
        self._cards = list(range(size))

    def shuffle(self, instructions):
        for instruction in instructions:
            if instruction.startswith('deal into new stack'):
                self.deal_stack()
            elif instruction.startswith('deal with increment'):
                self.deal(int(instruction[20:]))
            elif instruction.startswith('cut'):
                self.cut(int(instruction[4:]))
            else:
                raise ValueError(instruction)

    def deal_stack(self):
        self._cards.reverse()

    def cut(self, n):
        self._cards = self._cards[n:] + self._cards[:n]

    def deal(self, n):
        length = len(self._cards)
        result = [0] * length
        for i in range(length):
            result[(i * n) % length] = self._cards[i]
        self._cards = result

    def position_of(self, card):
        return self._cards.index(card)


with open('./input.txt', 'r') as f:
    program = f.readlines()
deck = Deck(10007)
deck.shuffle(program)
print(deck.position_of(2019))

deck = Deck(119315717514047)
for i in range(101741582076661):
    deck.shuffle(program)
print(deck.position_of(2019))
