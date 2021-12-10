from collections import defaultdict
def part_2(data):
    l = data
    map = defaultdict(int)
    for i in l:
        if i not in l:
            map[i] = 0;
        map[i]+=1
    print(map)
    for _ in range(256):
        k = defaultdict(int)
        for x, cnt in map.items():
            if x == 0:
                k[6] += cnt
                k[8] += cnt
            else:
                k[x-1] += cnt
        map = k
    print(sum(map.values()))


def part_1(data):
    l = data
    count = 0
    while count < 256:
        flag = False
        for i in range(len(l)):
            if l[i] == 0:
                l[i] = 6
                flag = True
            else:
                l[i] -= 1
            if flag:
                l.append(8)
                flag = False

        print(l)
        count += 1
    print(len(l))

def parse(data):
     l = []
     for i in data:
         for j in i.split(','):
             l.append(int(j))
     return l


with open('inputs.txt', 'r') as fh:
    d = fh.read().splitlines()
    data = parse(d)
    #data = [3,4,3,1,2]
    #part_1(data)
    part_2(data)