import sys


class Directory:

    def __init__(self, name, parent):
        self.name = name
        self.children = {}
        self.parent = parent
        self.size = 0


class File:

    def __init__(self, size, name, parent):
        self.parent = parent
        self.size = size
        self.name = name


root_dir = Directory('/', None)
listing = False

with open(sys.argv[1], 'r') as f:
    curr_dir = root_dir
    for line in f.readlines()[1:]:
        line = line.strip()

        if line.startswith("$ cd"):
            _, cd, dirname = line.split(' ')
            if dirname == '..':
                curr_dir = curr_dir.parent
            else:
                curr_dir = curr_dir.children.get(dirname)

        if line.startswith('dir'):
            _, dirname = line.split(' ')
            dir_ = Directory(dirname, curr_dir)
            curr_dir.children[dirname] = dir_

        if not line.startswith("$") and not line.startswith("dir"):
            size, fname = line.split(' ')
            f = File(int(size), fname, curr_dir)
            curr_dir.children[fname] = f


size_sum = 0
sizes = []


def dfs(directory):
    global size_sum
    global sizes
    for child in directory.children.values():
        if isinstance(child, File):
            directory.size += child.size

        if isinstance(child, Directory):
            size = dfs(child)
            sizes.append(size)
            directory.size += size

    if directory.size <= 100000:
        size_sum += directory.size
    return directory.size


dfs(root_dir)
print(size_sum)

# part 2
FS_SIZE = 70000000
SPACE_NEEDED = 30000000
SPACE_AVAILABLE = FS_SIZE - root_dir.size
SPACE_DIFF = SPACE_NEEDED - SPACE_AVAILABLE

sizes = filter(lambda x: x >= SPACE_DIFF, sizes)
print(sorted(sizes)[0])



