from collections import defaultdict, deque, Counter
def part_2(data):
    first = data[0]
    second = data[1:][0]

    MAX = 40
    t = Counter()
    for i in range(len(first)-1):
        t[first[i] + first[i+1]] += 1

    for j in range(MAX):
        s = Counter()
        for k in t:
            s[k[0] + second[k]] += t[k]
            s[second[k] + k[1]] += t[k]
        t = s

    x = Counter()
    for k in t:
        x[k[0]] += t[k]
    x[first[-1]] += 1

    print(max(x.values()) - min(x.values()))

def part_1(data):
    first = data[0]
    second = data[1:][0]
    MAX = 10
    for index in range(MAX):
        temp = first
        k = []
        for i in range(len(temp)):
            if len(temp[i:i+2]) == 2:
                k.append(temp[i])
                k.append(second[temp[i:i+2]])
        k.append(temp[-1])
        first = ''.join(k)
        if index == MAX - 1:
            pass
            print(first)

    c = Counter(first)
    print(max(c.values()) - min(c.values()))



def parse(data):
    l = []
    t = {}
    for i in data:
        if len(i) > 0:
            if '->' in i:
                x,y = i.split('->')
                t[x.strip()] = y.strip()
            else:
                l.append(i)
    l.append(t)
    return l



with open('inputs.txt', 'r') as fh:
    d = fh.read().splitlines()
    data = parse(d)

    #part_1(data)
    part_2(data)

#2911561572630