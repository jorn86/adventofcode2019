def grouped(p):
    return p[0] == p[1] or p[1] == p[2] or p[2] == p[3] or p[3] == p[4] or p[4] == p[5]


def test(p):
    d1 = int(p[0])
    d2 = int(p[1])
    d3 = int(p[2])
    d4 = int(p[3])
    d5 = int(p[4])
    d6 = int(p[5])
    if not d1 <= d2 <= d3 <= d4 <= d5 <= d6:
        return False
    return grouped([d1, d2, d3, d4, d5, d6])


begin = 138307
end = 654504
count = 0
for pw in range(begin, end + 1):
    if test(str(pw)):
        count += 1
print(count)
