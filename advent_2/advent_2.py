def part_2(data):
    s = 0
    m = 0
    aim = 0
    for i in data:
        k, v = i.split(' ')
        val = int(v)
        if k == 'forward':
            s += val
            aim += (m * val)
        if k == 'up':
            m -= val
        if k == 'down':
            m += val
    print(aim * s)


def part_1(data):
    s = 0
    m = 0
    for i in data:
        k, v = i.split(' ')
        val = int(v)
        if k == 'forward':
            s += val
        if k == 'up':
            m -= val
        if k == 'down':
            m += val
    print(m * s)


with open('inputs.txt', 'r') as fh:
    data = fh.read().splitlines()

    part_1(data)
    part_2(data)
