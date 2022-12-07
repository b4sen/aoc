import sys


num = 0
overlap = 0


def create_range(line_range):
    r1, r2 = line_range.split('-')
    return set(range(int(r1), int(r2)+1))


with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        l1, l2 = line.strip().split(',')
        l1 = create_range(l1)
        l2 = create_range(l2)
        if l1.issubset(l2) or l2.issubset(l1):
            num += 1
        if len(l1.intersection(l2)) > 0:
            overlap += 1


print(num)
print(overlap)
