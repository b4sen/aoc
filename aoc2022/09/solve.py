import sys

lines = open(sys.argv[1], "r").read().strip().split("\n")

h_pos = [0, 0]
t_pos = [0, 0]


mapper = {
    "R": [1, 0],
    "L": [-1, 0],
    "U": [0, 1],
    "D": [0, -1],
}

coords = []


def check_tail(head, tail):
    x_diff = head[0] - tail[0]
    y_diff = head[1] - tail[1]
    if max(abs(x_diff), abs(y_diff)) > 1:
        if x_diff > 0:
            tail[0] += 1
        elif x_diff < 0:
            tail[0] -= 1

        if y_diff > 0:
            tail[1] += 1
        elif y_diff < 0:
            tail[1] -= 1


for line in lines:
    dir_, n = line.split(" ")
    n = int(n)
    factor = mapper[dir_]
    for i in range(n):
        h_pos[0] += factor[0]
        h_pos[1] += factor[1]
        check_tail(h_pos, t_pos)
        coords.append(tuple(t_pos))


print(len(set(coords)))
# part 2
coords = []
rope = [[0, 0] for i in range(10)]
for line in lines:
    dir_, n = line.split(" ")
    n = int(n)
    factor = mapper[dir_]
    for i in range(n):
        rope[0][0] += factor[0]
        rope[0][1] += factor[1]
        for j in range(1, len(rope)):
            check_tail(rope[j-1], rope[j])
        coords.append(tuple(rope[-1]))


print(len(set(coords)))
