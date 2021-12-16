from collections import defaultdict, deque, Counter
def part_2(data):
    l = part_1(data)
    print(l)
    X = max([x for x,y in l.keys()])
    Y = max([y for x,y in l.keys()])

    ans = ''
    for y in range(Y+1):
        for x in range(X+1):
            ans += ('x' if (x,y) in l else ' ')
        print(ans)
        ans = ''
    print(ans)

def part_1(data):
    l = {}
    for i in data:
        if len(i) > 2:
            for m,n in i:
                l2 = {}
                key = m
                val = n
                if key == 'x':
                    for (x,y) in l:
                        if x < val:
                            l2[(x,y)] = True
                        else:
                            l2[((val - (x-val)), y)] = True
                else:
                    for (x, y) in l:
                        if y < val:
                            l2[(x, y)] = True
                        else:
                            l2[(x, (val - (y - val)))] = True
                l = l2
        else:
            m,n = i
            l[(m, n)] = True
    return l


def parse(data):
    l = []
    t = []
    for i in data:
        if 'fold' in i:
            t.append([i.split('=')[0][-1] , int(i.split('=')[1])])
        elif len(i) > 0:
            l.append([int(j) for j in i.split(',')])
    l.append(t)
    return l


with open('inputs.txt', 'r') as fh:
    d = fh.read().splitlines()
    data = parse(d)

    part_1(data)
    part_2(data)

# #PERCGJPB