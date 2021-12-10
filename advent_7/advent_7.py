import sys

def part_2(data):
    m = sys.maxsize
    for mid in range(max(data)):
        s = 0
        for i in data:
            k = abs(i - mid)
            s += k*(k+1)//2
        m = min(m, s)
    print(m)


def part_1(data):
    l = sorted(data)
    k = sum([abs(i-l[len(l)//2]) for i in l])
    print(k)


def parse(data):
    l = []
    for i in data:
        for j in i.split(','):
            l.append(int(j))
    return l


with open('inputs.txt', 'r') as fh:
    d = fh.read().splitlines()
    data = parse(d)

    part_1(data)
    part_2(data)