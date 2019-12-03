def fuel(mass):
    fuel = (mass // 3) - 2
    return fuel if fuel > 0 else 0


def total_fuel(mass):
    total = 0
    add = fuel(mass)
    while add > 0:
        total += add
        add = fuel(add)
    return total


def run(counter):
    total = 0
    for mass in open('./input.txt', 'r').readlines():
        total += counter(int(mass))
    return total


print(run(fuel))        # part 1
print(run(total_fuel))  # part 2
