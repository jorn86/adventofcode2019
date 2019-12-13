orbits = [(s[:3], s[4:7]) for s in open('./input.txt', 'r').readlines()]


def add_counts(counts, param):
    for o in orbits:
        if o[0] == param:
            counts[o[1]] = counts[o[0]] + 1
            add_counts(counts, o[1])


def path_from_root(start):
    if start == 'COM':
        return ['COM']
    for o in orbits:
        if o[1] == start:
            return path_from_root(o[0]) + [start]


counts = {'COM': 0}
add_counts(counts, 'COM')
print(sum(counts.values()))

you = path_from_root('YOU')
san = path_from_root('SAN')
for i in range(0, min(len(you), len(san))):
    if you[i] != san[i]:
        common_to_you = len(you) - i - 1  # don't count YOU
        common_to_san = len(san) - i - 1  # don't count SAN
        print(common_to_san + common_to_you)
        exit()
