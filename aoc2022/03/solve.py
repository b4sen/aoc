import sys
import string

l = string.ascii_lowercase + string.ascii_uppercase


lines = []
with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        lines.append(line.strip())

pts = 0
for line in lines:
    l1, l2 = set(line[:len(line)//2]), set(line[len(line)//2:])
    intersect = l1.intersection(l2)
    for ch in intersect:
        pts += l.index(ch) + 1

print(pts)

pts = 0
for i in range(0, len(lines), 3):
    a = set(lines[i])
    b = set(lines[i+1])
    c = set(lines[i+2])
    badge = a.intersection(b.intersection(c))
    for ch in badge:
        pts += l.index(ch) + 1

print(pts)
