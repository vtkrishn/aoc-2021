def part_2(data):
    R = len(data)
    C = len(data[0])

    def rec(i, j):
        global ans
        ans += 1
        data[i][j] = -1
        for dr in [-1,0,1]:
            for dc in [-1, 0, 1]:
                rr = i + dr
                cc = j + dc
                if 0 <= rr < len(data) and 0 <= cc < len(data[0]) and data[rr][cc] != -1:
                    data[rr][cc] += 1
                    if data[rr][cc] >= 10:
                        rec(rr, cc)

    t = 0
    while True:
        t +=1
        for i in range(R):
            for j in range(C):
                data[i][j] += 1
        for i in range(R):
            for j in range(C):
                if data[i][j] == 10:
                    rec(i, j)
        flag = True
        for i in range(R):
            for j in range(C):
                if data[i][j] == -1:
                    data[i][j] = 0
                else:
                    flag = False
        if flag:
            print(t)
            break
    #print(ans)

def part_1(data):
    R = len(data)
    C = len(data[0])

    def rec(i, j):
        global ans
        ans += 1
        data[i][j] = -1
        for dr in [-1,0,1]:
            for dc in [-1, 0, 1]:
                rr = i + dr
                cc = j + dc
                if 0 <= rr < len(data) and 0 <= cc < len(data[0]) and data[rr][cc] != -1:
                    data[rr][cc] += 1
                    if data[rr][cc] >= 10:
                        rec(rr, cc)

    for w in range(100):
        for i in range(R):
            for j in range(C):
                data[i][j] += 1
        for i in range(R):
            for j in range(C):
                if data[i][j] == 10:
                    rec(i, j)
        for i in range(R):
            for j in range(C):
                if data[i][j] == -1:
                    data[i][j] = 0
    print(ans)


def parse(data):
    l = []
    t = []
    for i in range(len(data)):
        for j in range(len(str(data[i]))):
            t.append(int(data[i][j]))
        l.append(t)
        t = []
    return l


with open('inputs.txt', 'r') as fh:
    ans = 0
    d = fh.read().splitlines()
    data = parse(d)

    #part_1(data)
    part_2(data)