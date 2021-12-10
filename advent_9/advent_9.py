def part_2(data):
    l = []
    for i in data:
        l.append([int(i) for i in list(i.strip())])

    k = []
    s = set()
    R, C = len(l), len(l[0])
    dd = [[-1,0],[0,1],[1,0],[0,-1]]
    for r in range(R):
        for c in range(C):
            if (r,c) not in s and l[r][c] != 9:
                size = 0
                q = []
                q.append((r,c))
                while q:
                    r,c = q.pop(0)
                    if (r,c) in s: continue
                    s.add((r, c))
                    size += 1
                    for d in dd:
                        rr, cc = r + d[0], c + d[1]
                        if 0 <= rr < R and 0 <= cc < C and l[rr][cc] != 9:
                            q.append((rr,cc))
                k.append(size)
    k.sort()
    print(k[-1]*k[-2]*k[-3])



def part_1(data):

    l = []
    for i in data:
        l.append([int(i) for i in list(i.strip())])

    R,C = len(l), len(l[0])
    dd = [[-1,0],[0,1],[1,0],[0,-1]]
    k = 0
    for r in range(R):
        for c in range(C):
            flag = True
            for d in dd:
                rr,cc = r + d[0], c + d[1]
                if 0 <= rr < R and 0 <= cc < C and l[rr][cc] <= l[r][c]: flag = False
            if flag: k += l[r][c]+1
    print(k)


def parse(data):
    return data


with open('inputs.txt', 'r') as fh:
    d = fh.read().splitlines()
    data = parse(d)

    part_1(data)
    part_2(data)