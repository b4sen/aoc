import sys

with open(sys.argv[1], 'r') as f:
    chars = f.read().strip()

# p1
for i in range(len(chars)):
    chs = set(chars[i:(i+4)])
    if len(chs) == 4:
        print(i+4)
        break

# p2
for i in range(len(chars)):
    chs = set(chars[i:(i+14)])
    if len(chs) == 14:
        print(i+14)
        break
