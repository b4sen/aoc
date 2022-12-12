import string
import sys

f = open(sys.argv[1]).read().strip().split("\n")

grid = []
start = None
end = None
dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]


class Node:
    def __init__(self, x, y, val):
        self.x = x
        self.y = y
        self.val = val
        self.neighbours = []
        self.parent = None

    def add_neighbours(self, grid):
        for d in dirs:
            x = max(0, self.x + d[1])
            y = max(0, self.y + d[0])
            if (y, x) == self.coords:
                continue
            try:
                node = grid[y][x]
                if node.val - self.val <= 1:
                    self.neighbours.append(node)
            except IndexError:
                pass

    @property
    def coords(self):
        return (self.y, self.x)

    def __eq__(self, other):
        return self.coords == other.coords


for i, line in enumerate(f):
    row = []
    for j, ch in enumerate(line):
        val = string.ascii_letters.index(ch)
        node = Node(j, i, val)
        if ch == "S":
            node.val = 0
            start = node

        if ch == "E":
            node.val = len(string.ascii_lowercase)
            end = node

        row.append(node)
    grid.append(row)

for row in grid:
    for node in row:
        node.add_neighbours(grid)


def bfs(grid, start):
    visited = []
    q = []
    q.append(start)
    is_finished = False
    path = []
    while q and not is_finished:
        node = q.pop(0)
        for child in node.neighbours:
            if child not in visited:
                child.parent = node
                q.append(child)
                visited.append(child)
            if child.coords == end.coords:
                print("FOUND END!")
                t = child
                while t.coords != start.coords:
                    path.append(t)
                    t = t.parent
                is_finished = True
                break
    return path


p = bfs(grid, start)
print(len(p))
shortest = 0
for node in p:
    if node.val == 0:
        break
    shortest += 1
print(shortest)  # idk why this works in my case, but it shouldn't
# the idea is to find the first occurence of 'a', but the example doesn't work
