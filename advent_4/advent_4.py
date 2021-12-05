def part_2(data):
    first = data[0]
    second = data[1:]

    def iswinning(jj, me):
        def trans(me):
            l = []
            for j in range(len(me)):
                t = []
                for k in range(len(me[0])):
                    t.append(me[k][j])
                l.append(t)
            return l

        def idfy(me):
            k = 0
            for i in me:
                for j in i:
                    if j < 0:
                        k += 1
                if k == 5:
                    if -jj not in i: return False
                    s = 0
                    for f in me:
                        if f == i:
                            print(i)
                        else:
                            s += sum([u for u in f if u > 0])
                    ff = s * jj
                    if ff <= 0: return False
                    print(jj, ff)
                    return True
                else:
                    k = 0
            return False

        return idfy(me) or idfy(trans(me))

    def check(i, j):
        k = 0
        for item in j:
            for e in range(len(item)):
                if item[e] == i or item[e] == 0:
                    item[e] = -i
        k += 1
        if iswinning(i, j):
            return True


    t = set()
    k = 1
    for i in first:
        for j in second:
            if k not in t and check(i, j):
                t.add(k)
                if len(t) == len(second):
                    return True
            k += 1
            k  = k % len(second)


def part_1(data):
    first = data[0]
    second = data[1:]


    def iswinning(jj, me):
        def trans(me):
            l = []
            for j in range(len(me)):
                t = []
                for k in range(len(me[0])):
                    t.append(me[k][j])
                l.append(t)
            return l

        def idfy(me):
            k = 0
            for i in me:
                for j in i:
                    if j < 0:
                        k+=1
                if k == 5:
                    s = 0
                    for f in me:
                        if f == i:
                            print(i)
                        else:
                            s += sum([u for u in f if u > 0])
                    print(jj, s * jj)
                    return True
                else:
                    k = 0
            return False

        return idfy(me) or idfy(trans(me))




    def check(i, j):
        k = 0
        for item in j:
            for e in range(len(item)):
                if item[e] == i or item[e] == 0:
                    item[e] = -i
        k += 1
        if iswinning(i, j):
            return True

    t = 0
    for i in first:
        for j in second:
            if check(i, j):
                t = 1
                break
        if t == 1:
            break





def parse(data):

    first, second = data[0], data[1:]
    second = [i for i in data[1:] if len(i) > 0]

    lis = [list(int(i.strip()) for i in first.split(','))]
    b = []
    for i in range(len(second)):
        if i != 0 and i % 5 == 0:
            lis.append(b)
            b = []
        b.append([int(j.strip()) for j in second[i].split(' ') if len(j) > 0])
    lis.append(b)
    return lis


with open('inputs.txt', 'r') as fh:
    d = fh.read().splitlines()
    part_1(parse(d))
    part_2(parse(d))