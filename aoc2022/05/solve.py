import sys
from collections import defaultdict
import re
import copy

moves = []

crates = defaultdict(list)


def process_movement(line):
    return re.sub(r"[a-z]", '', line)


def process_crates(line):
    for i in range(0, len(line), 4):
        num = line[i:(i+4)]
        num = num.strip().replace('[', '').replace(']','').replace(' ','')
        if not num.isnumeric() and num != '':
            crates[(i//4) + 1].append(num)


with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        if line.startswith('move'):
            line = process_movement(line.strip())
            _, num, _, from_, _, to_ = (line.split(' '))
            moves.append([int(num), int(from_), int(to_)])

        elif line == '\n':
            pass
        else:
            process_crates(line)

for k, v in crates.items():
    crates[k] = v[::-1]


crates_2 = copy.deepcopy(crates)


# part 1
for move in moves:
    n, from_, to_ = move
    for i in range(n):
        val = crates[from_].pop()
        crates[to_].append(val)

last = []
for k in sorted(crates.keys()):
    last.append(crates[k][-1])


print(''.join(last))

# part 2
for move in moves:
    n, from_, to_ = move
    to_move = []
    to_move = crates_2[from_][-n:]
    del crates_2[from_][-n:]
    crates_2[to_].extend(to_move)

last = []
for k in sorted(crates_2.keys()):
    last.append(crates_2[k][-1])

print(''.join(last))
