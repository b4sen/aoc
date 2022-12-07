import sys


mapper = {
    "X": ["A", 1, "B"],
    "Y": ["B", 2, "C"],
    "Z": ["C", 3, "A"],
}

mapper2 = {
    "A": ["B", "C"],
    "B": ["C", "A"],
    "C": ["A", "B"],
}

points = {
    "A": 1,
    "B": 2,
    "C": 3,
}


with open(sys.argv[1], 'r') as f:
    lines = [line.strip() for line in f.readlines()]

pts = 0
for line in lines:
    e, p = line.strip().split(' ')
    p, pt, beats = mapper[p]
    pts += pt
    if e == p:
        pts += 3
    elif e == beats:
        pts += 0
    else:
        pts += 6


print(pts)

pts = 0
for line in lines:
    e, p = line.split(' ')
    if p == "X":
        w, l = mapper2[e]
        pts += points[l]

    elif p == "Y":
        pts += points[e]
        pts += 3

    else:
        w, l = mapper2[e]
        pts += points[w]
        pts += 6

print(pts)
