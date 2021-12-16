from collections import defaultdict, deque
def part_2(data):
    l = defaultdict(list)
    for x, y in data:
        l[x].append(y)
        l[y].append(x)

    start = ('start', set(['start']), None)
    k = 0
    q = deque([start])
    while q:
        i, j, t = q.popleft()
        if i == 'end':
            k += 1
            continue
        for y in l[i]:
            if y not in j:
                ns = set(j)
                if y.lower() == y:
                    ns.add(y)
                q.append((y, ns, t))
            elif y in j and t is None and y not in ['start','end'] and not False:
                q.append((y, j, y))

    print(k)


def part_1(data):
    l = defaultdict(list)
    for x,y in data:
        l[x].append(y)
        l[y].append(x)

    start = ('start', set(['start']))
    k = 0
    q = deque([start])
    while q:
        i, j = q.popleft()
        if i == 'end':
            k += 1
            continue
        for y in l[i]:
            if y not in j:
                ns = set(j)
                if y.lower() == y:
                    ns.add(y)
                q.append((y, ns))
    print(k)




def parse(data):
    l = []
    for i in data:
        l.append(i.split('-'))
    return l


with open('inputs.txt', 'r') as fh:
    d = fh.read().splitlines()
    data = parse(d)

    part_1(data)
    part_2(data)