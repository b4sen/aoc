import sys
from copy import deepcopy
# sys.set_int_max_str_digits(9999999)
f = open(sys.argv[1]).read().strip().split('\n')

monkeys = {}


class Monkey:

    def __init__(self, id_, items, operation, test_num, throw_dict):
        self.id = id_
        self.items = items
        self.test_num = test_num
        self.throw_dict = throw_dict
        self.inspect_count = 0
        self.operation = operation  # e.g: '{} * 19'.format(item)

    def inspect(self, monkeys):
        for i, item in enumerate(self.items):
            self.inspect_count += 1
            item = eval(self.operation.replace('{}', str(item)))
            item = item // 3
            check = item % self.test_num == 0
            monkey_id = self.throw_dict[check]
            monkey = monkeys[monkey_id]
            monkey.items.append(item)
        self.items = []

    def inspect2(self, monkeys, modulo):
        for i, item in enumerate(self.items):
            self.inspect_count += 1
            item = int(item) % modulo
            item = eval(self.operation.replace('{}', str(item)))
            check = item % self.test_num == 0
            monkey_id = self.throw_dict[check]
            monkey = monkeys[monkey_id]
            monkey.items.append(item)
        self.items = []


modulo = 1
for i in range(0, len(f), 7):
    lines = f[i:i+7]
    monkey_id = int(lines[0][7])
    items = lines[1].split(':')[1].replace(' ', '').split(',')
    operation = lines[2].split('=')[1].strip().replace('old', '{}')
    test_num = int(lines[3].split('by ')[1].strip())
    modulo *= test_num
    throw_dict = {}
    throw_dict[True] = int(lines[4].split('monkey ')[1].strip())
    throw_dict[False] = int(lines[5].split('monkey ')[1].strip())
    monkey = Monkey(monkey_id, items, operation, test_num, throw_dict)
    monkeys[monkey_id] = monkey


p2 = deepcopy(monkeys)

# p1
for i in range(20):
    for idx, monkey in monkeys.items():
        monkey.inspect(monkeys)

max2 = sorted(monkeys.values(), key=lambda m: m.inspect_count, reverse=True)
print(max2[0].inspect_count * max2[1].inspect_count)


# p2
for i in range(10000):
    for idx, monkey in p2.items():
        monkey.inspect2(p2, modulo)

max2 = sorted(p2.values(), key=lambda m: m.inspect_count, reverse=True)
print(max2[0].inspect_count * max2[1].inspect_count)
