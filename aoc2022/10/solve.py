import sys

f = open(sys.argv[1], 'r').read().strip().split('\n')

cycle = 0
register = 1
sprite = ''
res = 0

for line in f:
    if line.startswith('a'):
        r = 2
        val = int(line.split(' ')[1])
    else:
        val = 0
        r = 1

    for i in range(r):
        if register - (cycle % 40) in [0, 1, -1]:
            sprite += '#'
        else:
            sprite += '.'
        cycle += 1
        if cycle == 20 or (cycle - 20) % 40 == 0:
            res += cycle * register


    register += val

print(res)
for i in range(0, len(sprite), 40):
    print(sprite[i:i+40])
