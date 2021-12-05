from collections import defaultdict
def part_2(data):
    s = defaultdict(int)
    for x1,y1,x2,y2 in data:
        dist1 = x2-x1
        dist2 = y2-y1

        for i in range(1 + max(abs(dist1), abs(dist2))):
            x = x1 + (1 if dist1 > 0 else (-1 if dist1 < 0 else 0)) * i
            y = y1 + (1 if dist2 > 0 else (-1 if dist2 < 0 else 0)) * i
            s[(x, y)] += 1
    print(sum([1 for k in s if s[k] > 1]))



def part_1(data):
    s = {}
    for x1,y1,x2,y2 in data:
        x1,x2 = min(x1,x2), max(x1,x2)
        y1,y2 = min(y1,y2), max(y1,y2)
        if x1 == x2 or y1 == y2:
            for x in range(x1,x2+1):
                for y in range(y1,y2+1):
                    if (x,y) not in s:
                        s[(x,y)] = 0
                    s[(x,y)] += 1

    print(sum([1 for k in s if s[k] > 1]))

def parse(data):

    # data = [
    # '0,9 -> 5,9',
    # '8,0 -> 0,8',
    # '9,4 -> 3,4',
    # '2,2 -> 2,1',
    # '7,0 -> 7,4',
    # '6,4 -> 2,0',
    # '0,9 -> 2,9',
    # '3,4 -> 1,4',
    # '0,0 -> 8,8',
    # '5,5 -> 8,2']

    l = []
    for i in data:
        x,y = [j.split(',') for j in i.split(' -> ')]
        x0 = int(x[0].split(' ')[0])
        x1 = int(x[1].split(' ')[0])
        y0 = int(y[0].split(' ')[0])
        y1 = int(y[1].split(' ')[0])
        l.append([x0,x1,y0,y1])
    return l


with open('inputs.txt', 'r') as fh:
    d = fh.read().splitlines()
    data = parse(d)

    part_1(data)
    part_2(data)