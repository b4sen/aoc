import sys
from collections import defaultdict

with open(sys.argv[1], 'r') as f:
    sol = defaultdict(int)
    idx = 0
    for line in f.readlines():
        if line != "\n":
            sol[idx]+= int(line)
        else:
            idx += 1
s = sorted(sol.values(), reverse=True)
print(s[0])
print(sum(s[:3]))
